import unittest
import localization


class TestLocalization(unittest.TestCase):

    def assertMatricesAlmostEqual(self, test, answer):
        for t_line, a_line in zip(test, answer):
            for t_value, a_value in zip(t_line, a_line):
                self.assertAlmostEqual(t_value, a_value)

    def test_one(self):
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'G'],
                  ['G', 'G', 'G']]
        measurements = ['R']
        motions = [[0, 0]]
        sensor_right = 1.0
        p_move = 1.0
        p = localization.localize(
            colors, measurements, motions, sensor_right, p_move)

        correct_answer = (
            [[0.0, 0.0, 0.0],
             [0.0, 1.0, 0.0],
             [0.0, 0.0, 0.0]])
        self.assertMatricesAlmostEqual(p, correct_answer)

    def test_two(self):
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        measurements = ['R']
        motions = [[0, 0]]
        sensor_right = 1.0
        p_move = 1.0
        p = localization.localize(
            colors, measurements, motions, sensor_right, p_move)
        correct_answer = (
            [[0.0, 0.0, 0.0],
             [0.0, 0.5, 0.5],
             [0.0, 0.0, 0.0]])
        self.assertMatricesAlmostEqual(p, correct_answer)

    def test_three(self):
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        measurements = ['R']
        motions = [[0, 0]]
        sensor_right = 0.8
        p_move = 1.0
        p = localization.localize(
            colors, measurements, motions, sensor_right, p_move)
        correct_answer = (
            [[0.06666666666, 0.06666666666, 0.06666666666],
             [0.06666666666, 0.26666666666, 0.26666666666],
             [0.06666666666, 0.06666666666, 0.06666666666]])
        self.assertMatricesAlmostEqual(p, correct_answer)

    def test_four(self):
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        measurements = ['R', 'R']
        motions = [[0, 0], [0, 1]]
        sensor_right = 0.8
        p_move = 1.0
        p = localization.localize(
            colors, measurements, motions, sensor_right, p_move)
        correct_answer = (
            [[0.03333333333, 0.03333333333, 0.03333333333],
             [0.13333333333, 0.13333333333, 0.53333333333],
             [0.03333333333, 0.03333333333, 0.03333333333]])
        self.assertMatricesAlmostEqual(p, correct_answer)

    def test_five(self):
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        measurements = ['R', 'R']
        motions = [[0, 0], [0, 1]]
        sensor_right = 1.0
        p_move = 1.0
        p = localization.localize(
            colors, measurements, motions, sensor_right, p_move)
        correct_answer = (
            [[0.0, 0.0, 0.0],
             [0.0, 0.0, 1.0],
             [0.0, 0.0, 0.0]])
        self.assertMatricesAlmostEqual(p, correct_answer)

    def test_six(self):
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        measurements = ['R', 'R']
        motions = [[0, 0], [0, 1]]
        sensor_right = 0.8
        p_move = 0.5
        p = localization.localize(
            colors, measurements, motions, sensor_right, p_move)
        correct_answer = (
            [[0.0289855072, 0.0289855072, 0.0289855072],
             [0.0724637681, 0.2898550724, 0.4637681159],
             [0.0289855072, 0.0289855072, 0.0289855072]])
        self.assertMatricesAlmostEqual(p, correct_answer)

    def test_seven(self):
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        measurements = ['R', 'R']
        motions = [[0, 0], [0, 1]]
        sensor_right = 1.0
        p_move = 0.5
        p = localization.localize(
            colors, measurements, motions, sensor_right, p_move)
        correct_answer = (
            [[0.0, 0.0, 0.0],
             [0.0, 0.33333333, 0.66666666],
             [0.0, 0.0, 0.0]])
        self.assertMatricesAlmostEqual(p, correct_answer)


if __name__ == '__main__':
    unittest.main()
