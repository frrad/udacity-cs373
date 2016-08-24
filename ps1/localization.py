def move(state, motion, p_move):
    x, y = motion[0], motion[1]
    x_length, y_length = len(state), len(state[0])
    for i in xrange(x_length):
        for j in xrange(y_length):
            state[i][j] = ((1 - p_move) * state[i][j] +
                           state[(i + x) % x_length][(j + y) & y_length] * p_move)


def measure(state, measurement, colors, sensor_right):
    for i in xrange(len(state)):
        for j in xrange(len(state[0])):
            if colors[i][j] == measurement:
                state[i][j] *= sensor_right
            else:
                state[i][j] *= (1 - sensor_right)
    normalize(state)


def normalize(matrix):
    normalizer = 1. / sum([sum(row) for row in matrix])
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[0])):
            matrix[i][j] *= normalizer


def localize(colors, measurements, motions, sensor_right, p_move):
    x, y = len(colors), len(colors[0])
    initial_probability = 1. / (x * y)
    state = [[initial_probability] * y for i in xrange(x)]
    for (measurement, motion) in zip(measurements, motions):
        move(state, motion, p_move)
        measure(state, measurement, colors, sensor_right)
    return state
