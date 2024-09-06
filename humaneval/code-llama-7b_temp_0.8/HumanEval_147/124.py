
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
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    # check n is valid
    if n < 1: return 0

    # initialize max_triples
    max_triples = 0
    # get all elements
    elements = []
    # iterate through numbers up to n
    for num in range(1, n + 1):
        # add num into elements array
        elements.append(num * num - num + 1)
    # iterate through elements
    for i in range(len(elements)):
        # iterate through elements[i+1:]
        for j in range(i+1, len(elements)):
            # iterate through elements[j+1:]
            for k in range(j+1, len(elements)):
                # get elements at i, j, k
                i_val = elements[i]
                j_val = elements[j]
                k_val = elements[k]
                # check if nums sum is divisible by 3
                if (i_val + j_val + k_val) % 3 == 0:
                    max_triples += 1
    return max_triples

    # Time Limit Exceeded
    # def get_max_triples(n):
    #     """
    #     You are given a positive integer n. You have to create an integer array a of length n.
    #         For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
    #         Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    #     and a[i] + a[j] + a[k] is a multiple of 3.

    #     Example :
    #         Input: n = 5
    #         Output: 1
    #         Explanation: 
    #         a = [1, 3, 7, 13, 21]
    #         The only valid triple is (1, 7, 13).
    #     """
    #     """
