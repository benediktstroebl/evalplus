
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    digit_map = {}
    count = 0
    for i in range(1, 10):
        digit_map[i] = 1
    for i in range(2, n + 1):
        digit_map[i] = 0
        for j in range(1, i):
            digit_map[i] += digit_map[j]
    for i in range(1, 10):
        if i == 1:
            count += digit_map[i]
        else:
            count += digit_map[i]
    return count

