def starts_one_ends(n):
    num = 10**n-1
    ones = num // 9 + 1
    ends_with_ones = num % 9
    return ones - ends_with_ones