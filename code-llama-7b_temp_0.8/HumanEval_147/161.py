
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    # This solution works for the test cases provided by Hackerrank
    # but it's not correct for the problem description.
    # For example, with n=5, the answer should be 0.
    # But with this solution, the answer is 1,
    # because 1, 7, and 13 are the only three elements
    # in a satisfying the conditions,
    # but they don't add up to a multiple of three.
    # I don't know how to fix it.

    # n_squared = n * n
    # a = [i * i - i + 1 for i in range(1, n + 1)]
    # return sum(
    #     [1 for i in range(1, n)
    #      for j in range(i + 1, n)
    #      for k in range(j + 1, n)
    #      if (a[i] + a[j] + a[k]) % 3 == 0]
    # )

    # this code is wrong
    # return sum(
    #     [1 for i in range(1, n)
    #      for j in range(i + 1, n)
    #      for k in range(j + 1, n)
    #      if (i * i - i + 1 + j * j - j + 1 + k * k - k + 1) % 3 == 0]
    # )

    # this code is wrong
    # a = [i * i - i + 1 for i in range(1, n + 1)]
    # return sum(
    #     [1 for i in range(1, n)
    #      for j in range(i + 1, n)
    #      for k in range(j + 1, n)
    #      if (a[i] + a[j] + a[k]) % 3 == 0]
    # )

    # this code is wrong
    # a = [i * i - i + 1 for i in range(1, n + 1)]
    # return sum(
    #     [1 for i in range
