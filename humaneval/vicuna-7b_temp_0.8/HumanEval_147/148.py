
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
    # Initialize the array a
    a = [i*i*i - i*i + 1 for i in range(n)]
    # Keep track of the number of triples
    triples = 0
    # Iterate through the array a
    for i in range(1, n):
        if (a[i] - a[i-1]) % 3 == 0:
            for j in range(i, n):
                if (a[j] - a[j-1]) % 3 == 0:
                    for k in range(j, n):
                        if (a[k] - a[k-1]) % 3 == 0:
                            triples += 1
    return triples
