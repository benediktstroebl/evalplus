def starts_one_ends(n):
    pos_num = 10**n - 10**(n - 1) + 1
    return pos_num - (pos_num - 9) / 9