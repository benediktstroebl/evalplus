
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Find the maximum n-digit integer, n, such that there exists one such
    # integer whose digits sum to n.
    n_max = 0
    while n_max < n:
        n_max += 1
        n_sum = sum([int(x) for x in str(n_max)])
        if n_sum == n:
            a, b = 0, 0
            for x in str(n_max):
                if x == '1':
                    a += 1
                else:
                    break
            for x in str(n_max)[::-1]:
                if x == '1':
                    b += 1
                else:
                    break
            return a + b


assert starts_one_ends(2) == 1
assert starts_one_ends(3) == 1
assert starts_one_ends(4) == 2
assert starts_one_ends(5) == 3
assert starts_one_ends(9) == 2
assert starts_one_ends(200) == 26
