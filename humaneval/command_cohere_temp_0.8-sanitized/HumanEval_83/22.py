def starts_one_ends(n):
    num = 10 ** (n - 1)
    ones = num - 1
    ends_with_one = ones % 10
    starts_with_one = ones // 10
    return starts_with_one + ends_with_one