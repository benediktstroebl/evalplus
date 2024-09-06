
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(1, n + 1):
        if i < 10:
            if i == 1:
                count += 1
            else:
                if i % 10 == 1:
                    count += 1
        else:
            if i >= 100:
                digit = i % 100
            else:
                digit = i % 10
            if digit == 1:
                count += 1
    return count

