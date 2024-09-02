
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

    def is_triple_multiple_3(n):
        # return True if n is multiple of 3
        return n % 3 == 0

    def get_triples(arr):
        # return number of triples satisfying the problem statement
        cnt = 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    if is_triple_multiple_3(arr[i] + arr[j] + arr[k]):
                        cnt += 1
        return cnt

    # Your code goes here
    return get_triples([i * i - i + 1 for i in range(1, n + 1)])

