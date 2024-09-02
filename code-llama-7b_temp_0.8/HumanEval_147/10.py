
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
        return (i * i - i + 1 for i in range(1, n + 1))

    def is_multiple_of_3(s):
        return s % 3 == 0

    def generate_triplets(triples):
        """
        A triplet (a, b, c) is valid iff:
            - a < b < c
            - a + b + c is a multiple of 3
        """
        for i, a in enumerate(triples):
            for b in triples[i + 1 :]:
                c = s - a - b
                if b < c and is_multiple_of_3(a + b + c):
                    yield (a, b, c)

    s = sum(get_triples(n))
    triplets = list(generate_triplets(get_triples(n)))
    return len(triplets)

