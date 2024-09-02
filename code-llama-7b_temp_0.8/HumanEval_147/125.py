
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
    # A = [0, 1, 2, 3, 4, 5]
    # A = [1, 4, 9, 16, 25, 36]
    # A = [1, 6, 13, 20, 27, 34]
    A = [1, 6, 13, 20, 27, 34]
    print(A)
    count = 0
    for i in range(0, len(A), 3):
        for j in range(i+1, len(A), 3):
            for k in range(j+1, len(A), 3):
                if (A[i] + A[j] + A[k]) % 3 == 0:
                    count += 1
    print(count)

