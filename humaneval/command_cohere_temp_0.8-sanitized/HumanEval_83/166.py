def starts_one_ends(n):
    num = 10 ** (n - 1)
    ones = num - 9
    ends_with_1 = ones * (ones + 1) // 2
    starts_with_1 = ones * ones
    return starts_with_1 + ends_with_1