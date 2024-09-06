
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
    # initialize array with 1 to n
    a = [1] * n
    # loop through the array
    for i in range(1, n):
        a[i] = (i * i - i + 1)
        # check if a[i] is a multiple of 3
        if (a[i] % 3) == 0:
            # loop through the array again and add i if i < j < k
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if j != k:
                        if a[j] + a[k] == a[i]:
                            return a[i]
    return 0
