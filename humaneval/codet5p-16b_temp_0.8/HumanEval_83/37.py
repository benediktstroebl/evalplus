
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    def count_starts_ends(num):
        count = 0
        if num < 10:
            if num == 1:
                count += 1
        else:
            if num % 10 == 1:
                count += 1
            if num % 10 == 0:
                count += 1
            for i in range(2, len(str(num)) + 1):
                digit = int(str(num)[:i])
                if digit % 10 == 1:
                    count += 1
                if digit % 10 == 0:
                    count += 1
        return count

    return sum([count_starts_ends(i) for i in range(1, n + 1)])

