def starts_one_ends(n):
    num = 10**n - 1
    ones = len(list(str(num)))
    ends_with_one = num % 10 == 1
    starts_with_one = True if n == 1 else num // 10 == 1
    return ones - (ends_with_one or starts_with_one)