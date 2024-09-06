
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 0:
        return 0

    endings = [0] * 2

    def calc_endings(num, n):
        if n == 0:
            return
        for i in range(num + 1, num * 10, 2):
            endings[i % 2] += 1
        calc_endings(num, n - 1)

    calc_endings(1, n)

    return endings[0] + endings[1]

