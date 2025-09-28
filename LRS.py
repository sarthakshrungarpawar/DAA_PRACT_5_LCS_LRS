UP = 'u'
LEFT = 's'
DIAG = 'd'
NONE = 'h'

class Cell:
    def __init__(self):
        self.val = 0
        self.dir = NONE

def LRS(a):
    m = len(a)
    c = [[Cell() for _ in range(m + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, m + 1):
            if a[i - 1] == a[j - 1] and i != j:
                c[i][j].val = c[i - 1][j - 1].val + 1
                c[i][j].dir = DIAG
            elif c[i - 1][j].val >= c[i][j - 1].val:
                c[i][j].val = c[i - 1][j].val
                c[i][j].dir = UP
            else:
                c[i][j].val = c[i][j - 1].val
                c[i][j].dir = LEFT

    return c

def getLRS(a, c, i, j):
    if i == 0 or j == 0:
        return ""
    if c[i][j].dir == DIAG:
        return getLRS(a, c, i - 1, j - 1) + a[i - 1]
    elif c[i][j].dir == UP:
        return getLRS(a, c, i - 1, j)
    else:
        return getLRS(a, c, i, j - 1)

def printCostMatrixWithDirection(c):
    print("\nCost Matrix with Directions:")
    for row in c:
        print(" ".join(f"{cell.val:2}{cell.dir}" for cell in row))


X = "AABCBDC"
c = LRS(X)
lrs_result = getLRS(X, c, len(X), len(X))
print("LRS:", lrs_result)
print("Length:", len(lrs_result))
printCostMatrixWithDirection(c)