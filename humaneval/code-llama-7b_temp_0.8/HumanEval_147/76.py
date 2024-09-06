
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
    # Edge Case
    if n == 1:
        return 0

    # a[i] = i*i - i + 1
    # a[i] + a[j] + a[k] is a multiple of 3
    # 1) (i*i - i) + (j*j - j) + (k*k - k) = 0
    # 2) (i*i - i + j*j - j) + (k*k - k) = 0
    # 3) (i*i - i + j*j - j + k*k - k) = 0

    # i is a factor of a[i]
    # i*i - i is a factor of a[i]

    # j is a factor of a[j]
    # j*j - j is a factor of a[j]

    # k is a factor of a[k]
    # k*k - k is a factor of a[k]

    # if i is a factor of a[i], and j is a factor of a[j], and k is a factor of a[k]
    # then i*i - i + j*j - j + k*k - k is a multiple of 3
    count = 0
    for i in range(1, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (i*i - i + j*j - j + k*k - k) % 3 == 0:
                    count += 1
    return count

