
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
    # we can create a dictionary to store the previous values of a[i]
    # then for each i, we can check the value at i-1, i+1 and i-2
    # if a[i-1]%3 == 0, then we can check if a[i-2] and a[i+1] are valid
    # same logic for a[i+1]
    # for i-2 and i+2, we need to check if a[i] is divisible by 3
    # if any of the a[i-1] or a[i+1] is not valid, then we need to check if a[i-2] or a[i+2] is valid
    
    a = [i**2 - i + 1 for i in range(1, n+1)]
    d = dict()
    triples = 0
    
    for i in range(1, n+1):
        # i-2
        if a[i-1]%3 == 0:
            if i-2 >= 1:
                if (a[i-2], a[i-1], a[i]) not in d.keys():
                    d[(a[i-2], a[i-1], a[i])] = 1
                    triples += 1
            if i+2 <= n:
                if (a[i], a[i+1], a[i+2]) not in d.keys():
                    d[(a[i], a[i+1], a[i+2])] = 1
                    triples += 1
        # i+2
        if i+2 <= n:
            if a[i+1]%3 == 0:
                if (a[i], a[i+1], a[i+2]) not in d.keys():
                    d[(a[i], a[i+1], a[i+2])] = 1
                    triples += 1
    
    return triples
