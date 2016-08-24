Quiz:
Localization Program
For the purpose of this homework assume that the robot can move only left, right, up, or down. It cannot move diagonally. Also, for this assignment, the robot will never overshoot its destination square it will either make the movement or it will remain stationary.

Warning:
If you define any helper functions make sure they do not rely on globally defined variables and take all their state as parameters.

Reminder:
Reference 1D sense and move functions developed during the lesson:


def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q


def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i - U) % len(p)]
        s = s + pOvershoot * p[(i - U - 1) % len(p)]
        s = s + pUndershoot * p[(i - U + 1) % len(p)]
        q.append(s)
    return q
