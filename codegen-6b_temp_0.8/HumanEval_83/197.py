
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    digit_to_count = {}
    for i in xrange(1, n):
        if i < 10:
            digit_to_count[i] = 1
        elif i < 100:
            digit_to_count[i] = sum(digit_to_count.get(i // 10, 0), digit_to_count.get(i % 10, 0))
        else:
            digit_to_count[i] = sum(digit_to_count.get(i // 100, 0), digit_to_count.get(i // 10 % 10, 0), digit_to_count.get(i % 10, 0))

    return sum(digit_to_count.values())

