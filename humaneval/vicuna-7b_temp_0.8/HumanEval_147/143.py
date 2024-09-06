
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
    # The array a is a list of integers from 1 to n.
    a = [i + 1 for i in range(n)]

    # The function checks if the array a has any triples that satisfy the condition.
    # It does this by iterating over the array a, checking if the values of a[i], a[j], and a[k] are a multiple of 3, and
    # if so, storing the triple in a list. If the condition is not satisfied, the function returns 0.
    return sum([1 for i in range(n) if any([a[i] % 3 == 0, a[j] % 3 == 0, a[k] % 3 == 0] for j in range(i+1, n))])
