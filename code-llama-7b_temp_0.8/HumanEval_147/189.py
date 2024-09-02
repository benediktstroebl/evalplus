
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
    # 1. Write down the solution in your own words.
    #   - Brute force:
    #       - Iterate through each array index 1 to n.
    #       - For each index, multiply the index by index - index + 1 to get the value of the index.
    #       - Check if a[i] * a[j] * a[k] is a multiple of 3
    #   - Optimize the brute force solution:
    #       - Iterate through each array index 1 to n.
    #       - Check if a[i] * a[j] * a[k] is a multiple of 3 for i < j < k
    #   - Optimize the brute force solution further:
    #       - Find a[i], a[j], a[k] for i < j < k and a[i] * a[j] * a[k] is a multiple of 3
    #       - Store a[i], a[j], a[k] in a hash set
    #       - Iterate through the values of a and check if a[i] * a[j] * a[k] is a multiple of 3
    #         if yes, return 3
    #       - If no, return 0
    #   - Optimize the brute force solution even further:
    #       - Check for i < j < k and a[i] * a[j] * a[k] is a multiple of 3 for each i and j
    #       - Store a[i] * a[j] in a hash set
    #       - Check for each k, a[k] * a[i] * a[j] is a multiple of 3, where i, j < k
    #         - If yes, return 6
    #       - If no, return 0
    #
    #
    # 2. Try to write out the steps in your solution.
    #
    #   - Brute force:
    #       1. Iterate through each array index 1 to n.
    #       2. For each index, multiply the index by index - index + 1 to get the value of the index.
    #       3. Check
