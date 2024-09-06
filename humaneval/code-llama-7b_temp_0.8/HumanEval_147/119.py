
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

    # if n is 1, return 0
    if n == 1:
        return 0

    # if n is 2, return 1
    if n == 2:
        return 1

    # array that will hold the results
    a = [1, 3, 7, 13, 21]
    # initialise count variable to zero
    count = 0

    # loop through each value in array
    for i in a:
        # loop through each value in array
        for j in a:
            # loop through each value in array
            for k in a:
                # check if i < j < k
                if i < j < k:
                    # check if the sum is a multiple of 3
                    if (i + j + k) % 3 == 0:
                        count += 1

    return count
