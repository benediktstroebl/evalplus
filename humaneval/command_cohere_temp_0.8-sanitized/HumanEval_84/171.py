def solve(n):
    binary_string = '1'
    while n > 0:
        n, r = divmod(n, 2)
        binary_string += str(r)
    return binary_string