
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
    if n < 3:
        return 0
    else:
        nums = [0] * (n * n)
        nums[2] = 1
        for i in range(3, n * n, 2):
            nums[i] = i % 3
        return nums.count(0)

assert get_max_triples(5) == 1
assert get_max_triples(7) == 3
assert get_max_triples(10) == 4
assert get_max_triples(100) == 25

