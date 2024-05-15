#!/usr/bin/python3
""" N queens problem """

import sys


def print_solution(board):
    """Print the solution"""
    n = len(board)
    solution = []
    for i in range(n):
        solution.append([i, board[i]])
    print(solution)


def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]"""
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True


def solve_n_queens(board, col, n):
    """Solve the n queens problem"""
    if col == n:
        print_solution(board)
        return
    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i
            solve_n_queens(board, col + 1, n)
            board[col] = -1


def n_queens(n):
    """Solve the n queens problem"""
    board = [-1 for _ in range(n)]
    solve_n_queens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    n_queens(n)
