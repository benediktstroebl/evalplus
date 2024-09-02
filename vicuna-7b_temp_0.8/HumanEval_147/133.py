
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
    # creating an empty list to store the triples
    triples = []
    # iterating over the range of values from 1 to n
    for i in range(1, n+1):
        # checking if i is a multiple of 3
        if i % 3 == 0:
            # checking if i-1 is less than j is less than k
            if i-1 < j and j < k:
                # adding the triple to the list
                triples.append((i-1, j, i))
    return len(triples)
