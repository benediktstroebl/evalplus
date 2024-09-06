
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
    # initialize an array a of length n with values i*i-i+1
    a = [i*i-i+1 for i in range(n)]
    # initialize a dictionary where the key is the index i and the value is the value of a[i]
    d = {}
    for i in range(n):
        if a[i] != i*i-i+1:
            return 0
        d[i] = a[i]
    # iterate over all the elements of a
    for i in range(n):
        # if a[i] is not in the dictionary, it means that i is the first element
        if a[i] not in d:
            # we start the iteration from this element and we continue until we find an element greater than i
            j = i
            while j < n and d[j] == a[j]:
                j += 1
            # if we found an element greater than i, it means that there is a triple
            if j > i:
                return j - i + 1
    # if we did not find any triple, we return 0
    return 0