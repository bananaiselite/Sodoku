

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


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
        # Check column
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


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - - - -')
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print('| ', end='')
            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], ' ', end='')


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)


if __name__ == '__main__':
    print_board(board)
    solve(board)
    print('========================')
    print_board(board)
