
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
    count = 0
    # your code goes here
    for i in range(1, n + 1):
        a = i * i - i + 1
        for j in range(i, n + 1):
            b = j * j - j + 1
            for k in range(j, n + 1):
                c = k * k - k + 1
                if a + b + c % 3 == 0:
                    count += 1
    return count

