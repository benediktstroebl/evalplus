
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    ways = [0]
    for i in range(1, n + 1):
        ways.append(ways[-1] + ways[-2])
    return ways[n]


"""
Follow up: What if the digits are not distinct?
For example, there are lots of   1   9   9   9   9   9   9  numbers
with   1   9   9   9   9   9   9   9   9  numbers,
so we have a lot of possibilities to decode.
"""
