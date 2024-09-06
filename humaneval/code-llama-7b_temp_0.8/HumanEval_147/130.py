
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
    def get_triples(n):
        res = []
        for i in range(1,n+1):
            res.append(i * i - i + 1)
        return res
    def get_triples_count(triples):
        count = 0
        for i in range(len(triples)):
            for j in range(i+1, len(triples)):
                for k in range(j+1, len(triples)):
                    if triples[i] + triples[j] + triples[k] % 3 == 0:
                        count += 1
        return count
    triples = get_triples(n)
    return get_triples_count(triples)
