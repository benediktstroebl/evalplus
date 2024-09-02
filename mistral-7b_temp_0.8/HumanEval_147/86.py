
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

    # Initialize the result as 0
    result = 0
    # Initialize the array with n elements
    a = [i * i - i + 1 for i in range(1, n + 1)]

    # Iterate through the array
    for i in range(len(a)):
        # Iterate through the array again
        for j in range(i + 1, len(a)):
            # Iterate through the array again
            for k in range(j + 1, len(a)):
                # Check if the sum of the triple is a multiple of 3
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    # If it is, increment the result by 1
                    result += 1
    # Return the result
    return result
