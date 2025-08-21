def solveSudoku(board):
    def is_valid(r, c, ch):
        # Check row
        for i in range(9):
            if board[r][i] == ch:
                return False
        # Check column
        for i in range(9):
            if board[i][c] == ch:
                return False
        # Check 3x3 subgrid
        box_row = (r // 3) * 3
        box_col = (c // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[box_row + i][box_col + j] == ch:
                    return False
        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":  # Empty cell
                    for ch in map(str, range(1, 10)):
                        if is_valid(r, c, ch):
                            board[r][c] = ch
                            if backtrack():  # Continue solving
                                return True
                            board[r][c] = "."  # Undo move
                    return False  # No valid number found
        return True  # Solved

    backtrack()
    return board


# Dummy board (your example)
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solution = solveSudoku(board)

# Print the solved Sudoku
for row in solution:
    print(row)
