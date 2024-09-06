
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

    def compute_triple(a):
        return sum(a) % 3

    def compute_triples(a):
        triple = 0
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                for k in range(j+1, len(a)):
                    if a[i] + a[j] + a[k] % 3 == 0:
                        triple += 1
        return triple

    def compute_triples_using_func(a):
        return sum(compute_triple(triple) for triple in combinations(a, 3))

    print(compute_triples_using_func([1, 3, 7, 13, 21]))
    print(compute_triples_using_func([7, 3, 2, 9, 11, 14, 10, 19, 13, 12, 8, 18, 17, 1, 4, 16, 15,
