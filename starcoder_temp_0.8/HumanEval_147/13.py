
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
    # # method 1
    # count = 0
    # for i in range(n):
    #     for j in range(n):
    #         if i < j:
    #             a, b = i * i - i + 1, j * j - j + 1
    #             if a % 3 == 0 and b % 3 == 0 and a + b % 3 == 0:
    #                 count += 1
    # return count

    # method 2
    return sum([i + j + k for i in range(n) for j in range(n) if i < j for k in range(n) if i < k < j and (i + j + k) % 3 == 0])

