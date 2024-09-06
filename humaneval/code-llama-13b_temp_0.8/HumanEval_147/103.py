
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
    res = 0
    mod = 3
    # One thing to note is that any number when divided by 3 must result in either 1, 2 or 0.
    # This is because, a % 3 = a - 3 * (a // 3)
    # Therefore, if a % 3 = 0, then a must be a multiple of 3. 
    # If a % 3 = 1, then 3 must be a divisor of a-1. 
    # If a % 3 = 2, then 3 must be a divisor of a+1. 
    dict_mod_3 = {0: 0, 1: 0, 2: 0}
    dict_pair_sums = {}
    for i in range(n):
        # Updating dict_mod_3
        # We have a[i] = i*i - i + 1
        # So, a[i] % 3 = (i*i - i) % 3 = (i*i) % 3 - i % 3
        # = ((i % 3) * (i % 3)) % 3 - (i % 3) % 3
        # = (i % 3) * (i % 3) % 3 - (i % 3) % 3
        # = (i % 3) * (i % 3) % 3 - (i % 3) % 3 + (i % 3) % 3
        # = (i % 3) * (i % 3) % 3
        # If a % 3 = 1, then 3 must be a divisor of a-1. 
        # So, (a-1) % 3 = 0. Which implies that (a-1) = 3 * k, for some integer k.
        # (a-1) = (i-1)*(i-1) - (i-1) + 1
        #       = (i*i - 2*i + 2) - (i-1) + 1
        #       = i*i - i + 1 - (i-1) + 1
        #
