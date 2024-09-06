def starts_one_ends(n):
    pos_int = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if n < 1 or n > 10:
        return 0
    if n == 1:
        return 1
    return sum(1 for x in range(n-1, 0, -1) if pos_int[x] == '1' or pos_int[n-x-1] == '1')