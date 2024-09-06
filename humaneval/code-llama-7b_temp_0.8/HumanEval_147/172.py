
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

    # Get the number of triples with sum 0, 3, 6, 9, 12, ...
    # For n triples with sum 0, n * (n - 1) * (n - 2) / 6 is needed.
    # For n triples with sum 3, n * (n - 1) * (n - 2) / 2 is needed.
    # For n triples with sum 6, n * (n - 1) * (n - 2) / 2 is needed.
    # For n triples with sum 9, n * (n - 1) * (n - 2) / 2 is needed.
    # For n triples with sum 12, n * (n - 1) * (n - 2) / 2 is needed.
    # These triples are added as 3 numbers with 3 * x numbers in the array.
    n_triples = n * (n - 1) * (n - 2) / 6

    # Get the number of triples with sum 0
    # Triples with sum 0 have the form (a[i], a[j], a[k]) where a[i] == a[j] == a[k].
    # A[i] has to be equal to a number i * i - i + 1.
    # a[i] * 3 = 3i * i - 3i + 1
    n_triples_0 = 3 * n_triples

    # Get the number of triples with sum 3
    # Triples with sum 3 have the form (a[i], a[j], a[k]) where a[i] == a[j] != a[k] or a[i] != a[j] == a[k].
    # The first case is the same as with the sum of 0.
    # For the second case, a[i] == a[j] != a[k].
    # In this case a[k] = 3 - a[i] - a[j].
    # The same conditions must be met as for the sum of 0 and 3.
    n_
