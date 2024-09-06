
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
    
    # make array a such that a[i] = i * i - i + 1
    a = [x for x in range(1,n+1)]
    
    # keep track of triples
    triple_count = 0

    # for each index, find the set of valid indices
    for i in range(len(a)):
        # a[i] * a[j] * a[k] = (a[i]+a[j]+a[k]) % 3
        # a[i] % 3 == 0
        # a[j] % 3 == 0
        # a[k] % 3 == 0
        # a[j] == a[k]
        j = i+1
        k = j+1
        while k < len(a) and j < len(a):
            if (a[i] + a[j] + a[k]) % 3 == 0 and a[i] % 3 == 0 and a[j] % 3 == 0 and a[k] % 3 == 0 and a[j] == a[k]:
                triple_count += 1
            j += 1
            k += 1
    
    return triple_count
