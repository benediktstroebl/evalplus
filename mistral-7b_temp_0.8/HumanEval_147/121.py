
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
    """
    We can use the following formula to generate the triples in O(1) time per triple:
        a[i] = a[i - 1] + 2 * i - 1
    Now, we can use the following formula to count the triples that sum up to a multiple of 3:
        sum(a[i]) % 3 == 0
    Then, we can use the following formula to count the number of valid triples:
        (n - 1) * (n - 2) * (n - 3) / 6
    Finally, we can use the following formula to count the total number of triples:
        (n - 1) * (n - 2) * (n - 3) / 6 - (n - 1) * (n - 2) / 6
    """
    def get_max_triples(n):
        # Create the array a of length n
        a = [i * i - i + 1 for i in range(1, n + 1)]

        # Count the number of triples that sum up to a multiple
