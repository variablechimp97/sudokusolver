from pprint import pprint

def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None # no empty spaces left

def is_valid(puzzle, guess, row, col):
    # checks whether the guess at row/col is a valid guess, returns True/False
    # checks rows
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    # checks columns
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    # checks 3x3 matrix around it
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    # is Valid
    return True


def solve_sudoku(puzzle):
    # choose somewhere on the board and make a guess
    row, col = find_next_empty(puzzle)
    # check if solved puzzle
    if row is None:
        return True

    for guess in range(1, 10):
        # check if valid guess
        if is_valid(puzzle, guess, row, col):
            # place guess on puzzle
            puzzle[row][col] = guess
            # recursively call function
            if solve_sudoku(puzzle):
                return True
        # if not valid OR if our guess does not solve puzzle
        puzzle[row][col] = -1 # reset the guess
    # none of the numbers work, then it's unsolvable
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
