
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    assert type(n) == int, 'n should be an integer.'
    assert n > 0, 'n should be a positive integer.'
    
    one_digits = range(1, 10)
    two_digits = range(10, 100)
    three_digits = range(100, 1000)
    count = 0

    if n == 1:
        count = len(one_digits)
    elif n == 2:
        for number in two_digits:
            if number % 10 == 1 or number // 10 == 1:
                count += 1
    elif n == 3:
        for number in three_digits:
            if number % 10 == 1 or number // 100 == 1:
                count += 1

    return count
