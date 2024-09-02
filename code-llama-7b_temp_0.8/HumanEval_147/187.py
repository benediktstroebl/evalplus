
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
    # Naive way
    # time O(n^3) space O(1)
    # for i in range(n):
    #     for j in range(i+1, n):
    #         for k in range(j+1, n):
    #             if i < j < k and (i*i - i + 1) + (j*j - j + 1) + (k*k - k + 1) % 3 == 0:
    #                 return 1

    # Optimize:
    # For a[i], a[j], a[k]:
    # a[i] + a[j] + a[k] = (i * i - i + 1) + (j * j - j + 1) + (k * k - k + 1)
    # a[i] + a[j] + a[k] = 3 * (i * j - i + 1) + 2 * (k - i)
    # a[i] + a[j] + a[k] = 3 * (i * j - i + 1) + 2 * (k - i)
    # 2 * (k - i) = (a[i] + a[j] + a[k]) - 3 * (i * j - i + 1)
    # 2 * (k - i) = 3 * (i * j - i + 1) - (a[i] + a[j] + a[k])
    # 2 * (k - i) = 3 * (i * j - i + 1) - 3 * (i * j - i + 1) + 2 * (k - i)
    # 0 = 2 * (k - i) - 2 * (k - i)
    # 0 = 0
    # time O(n^2) space O(1)
    # for i in range(n):
    #     for j in range(i+1, n):
    #         for k in range(j+1, n):
    #             if i < j < k and (i*i - i + 1) + (j*
