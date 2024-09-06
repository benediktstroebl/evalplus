
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
    # 1st Solution: Time Limit Exceeded
    """
    def helper(i, j, k, count):
        if i == j == k:
            return count
        if (i < j) and (j < k):
            count += (3*i + 3) * (3*j + 3) * (3*k + 3) / 9
            return helper(i+1, j, k, count)
        elif (i < j) and (j >= k):
            return helper(i+1, j, k, count)
        else:
            return helper(i, j+1, k, count)
    return helper(1, 1, 1, 0)
    """

    # 2nd Solution:
    def helper(n):
        count = 0
        for i in range(1, n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if (3*i + 3)*(3*j + 3)*(3*k + 3) % 9 == 0:
                        count += 1
        return count

    return helper(n)

