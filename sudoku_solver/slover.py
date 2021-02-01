
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        (row, col) = find
        for i in range(1, 10):
            if valid(bo, i, (row, col)):
                bo[row][col] = i

                if solve(bo):  # calling solve on new board
                    return True
            bo[row][col] = 0
    return False


def valid(bo, num, pos):
    """
    :param bo: Board Matrix
    :param num: int
    :param pos:tuple (row ,col)
    :return:
    """

    # check row
    for j in range(len(bo[0])):
        if bo[pos[0]][j] == num and pos[1] != j:
            return False
    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)


