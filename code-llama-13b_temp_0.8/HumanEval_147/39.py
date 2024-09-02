
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
    i = 1
    triples = 0
    while i < n:
        j = i + 1
        while j < n:
            k = j + 1
            while k < n:
                # print(i, j, k)
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    triples += 1
                k += 1
            j += 1
        i += 1
    return triples


    a.append(i*i-i+1)
