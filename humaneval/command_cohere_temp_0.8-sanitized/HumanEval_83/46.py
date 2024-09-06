def starts_one_ends(n):
    num = 10**n-1
    ones = len(list(str(num)))
    ends_with_one = ones - 2*n
    starts_with_one = ones - ends_with_one
    return starts_with_one + ends_with_one