
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
    # is a list even necessary?
    a = [i*i - i + 1 for i in range(1, n+1)]
    pairs = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            pairs.append((a[i], a[j]))
    triples = []
    for i in range(len(pairs)):
        for j in range(i+1, len(pairs)):
            if ((pairs[i][0] + pairs[i][1]) % 3 == 0 and (pairs[j][0] + pairs[j][1]) % 3 == 0):
                triples.append((pairs[i], pairs[j]))
    count = 0
    for t in triples:
        t1 = t[0][0] + t[0][1]
        t2 = t[1][0] + t[1][1]
        if t1 + t2 % 3 == 0:
            count += 1
    return count

