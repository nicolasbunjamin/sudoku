# shoutout to Thorsten Altenkirch (Computerphile) for inspiration (https://youtu.be/G_UYXzGuqvM)

board = [[6, 2, 7, 3, 5, 1, 9, 8, 4],
         [8, 1, 3, 4, 6, 9, 2, 5, 7],
         [5, 9, 4, 2, 8, 7, 6, 1, 3],
         [1, 7, 5, 9, 4, 6, 8, 3, 2],
         [0, 6, 9, 0, 2, 8, 0, 0, 0],
         [0, 0, 8, 0, 0, 0, 1, 0, 6],
         [7, 3, 0, 8, 0, 5, 4, 2, 0],
         [9, 0, 0, 7, 3, 0, 0, 6, 1],
         [4, 5, 1, 6, 9, 2, 3, 7, 8]]


def solver():
    # find empty
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == 0:
                for content in range(1, 10):
                    if check_input(row, column, content):
                        # fill the current cell
                        board[row][column] = content
                        print("Inputting ", str(content),
                              " in row ", str(row + 1),
                              " column ", str(column + 1))

                        # CODE NOT WRITTEN YET
                        # if board still contains 0...

                        solver()
                        # if there's no solution, set it back to 0...
                        board[row][column] = 0

                print("Oops! Backtracking...")  # ... then backtrack
                return

    # display the board again after the recursion stops
    print("")
    print("SOLVED:")
    display(board)
    print("DONE.")
    exit()


# you can import numpy to use matrix, or make your own:
def display(board):
    # apparently, you don't have to write list(range(len(board)))
    for row in range(len(board)):

        if row % 3 == 0:
            # prints an empty line before the sudoku start
            # (0 % 3 == 0)
            # also, prints an empty line before row 3 and 6
            # remember that row 3 is actually the 4th row
            print("")

        for column in range(len(board)):

            if column % 3 == 0:
                # prints an additional space between grids
                # again, remember that column 3 is the 4th column
                # the empty END key prevents the console
                # from starting a new line
                print("  ", end="")

            if column == 8:
                # prints column 8 (9th column), then start a new line
                print(board[row][column])
            else:
                # prints column 1 to 7
                # again, prints a space at the END without starting a new line
                print((board[row][column]), end=" ")
    print("")


# checks if the cell content adheres to sudoku rules
def check_input(row, column, content):
    # checks row
    for cells in (range(len(board))):
        if board[row][cells] == content:
            return False

    # checks column
    for cells in (range(len(board))):
        if board[cells][column] == content:
            return False

    # checks grid
    # generates grid row identifiers 0, 3, or 6
    # the // operator rounds down the division product
    grid_row = (row // 3) * 3
    # generates grid column identifiers 0, 3, or 6
    grid_column = (column // 3) * 3
    # range(3) is the constant for 9 by 9 sudoku
    for row_in_grid in (range(3)):  # locks the row within grid
        for column_in_grid in (range(3)):
            if board[grid_row + row_in_grid][grid_column + column_in_grid] \
                    == content:
                return False
    return True


display(board)
solver()
