
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

    def get_count(num):
        count = 0
        for i in range(1, num+1):
            count += 1
        return count

    def is_valid(a, b, c):
        return a + b + c % 3 == 0

    def get_valid_triples(a, count):
        valid_triples = 0
        for i in range(0, count):
            for j in range(i+1, count):
                for k in range(j+1, count):
                    if is_valid(a[i], a[j], a[k]):
                        valid_triples += 1
        return valid_triples

    a = list(range(1, n+1))
    count = get_count(n)
    return get_valid_triples(a, count)

