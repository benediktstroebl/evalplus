
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def helper(n, i):
        if n - i - 1 < 0 or n - i - 1 > len(num_list) - 1:
            return 0

        if i == 0:
            return 1 if num_list[n - i - 1] == '1' else 0

        if i == len(num_list):
            return 0

        return helper(n, i + 1) + helper(n, i - 1)

    num_list = [str(n + 1 - i) for i in range(n)]
    return helper(n, 0)


assert starts_one_ends(2) == 8
assert starts_one_ends(3) == 121
assert starts_one_ends(4) == 40585
assert starts_one_ends(5) == 95833
assert starts_one_ends(6) == 355880
