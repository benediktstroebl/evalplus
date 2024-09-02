
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    result = 0
    for i in range(n):
        temp = (n - i) * 10 ** i
        if temp > 10 ** (n - 1):
            continue
        if temp % 10 == 1 or temp % 10 == 9:
            result += 1
        if i > 0:
            if i + 1 < n:
                if temp // 10 ** (i - 1) % 10 == 1 or temp // 10 ** (i - 1) % 10 == 9:
                    result += 1
            if i + 2 < n:
                if temp // 10 ** i % 10 == 1 or temp // 10 ** i % 10 == 9:
                    result += 1
    return result

