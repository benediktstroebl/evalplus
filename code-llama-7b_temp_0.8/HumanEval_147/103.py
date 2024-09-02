
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
    # to find all possible 3 digit numbers
    # given n = 5
    # then i can be 1-5
    # for each i, k = i+1 to n
    # for each k, j = k+1 to n
    # a[i] + a[j] + a[k] will be a multiple of 3
    # so if we add these 3 numbers to a hashset
    # and then check for the number of elements in the hashset
    # the answer is the number of triples

    # O(n^3) time complexity
    # O(n) space complexity

    # given a = [1, 3, 7, 13, 21]
    # for each i, j = i+1 to n
    # for each j, k = j+1 to n
    # sum = a[i] + a[j] + a[k]
    # if sum is multiple of 3
    # then add the 3 numbers to a hashset
    # return number of elements in the hashset
    # a[i] = i*i - i + 1
    # a[j] = (i+1)*(i+1) - (i+1) + 1
    # a[k] = (i+2)*(i+2) - (i+2) + 1
    # a[i] + a[j] + a[k] = (i*i - i + 1) + ((i+1)*(i+1) - (i+1) + 1) + ((i+2)*(i+2) - (i+2) + 1)
    #               = i^2 + 2i + 1 + (i+1)^2 + 2(i+1) + 1 + (i+2)^2 + 2(i+2) + 1
    #               = 3i^2 + 6i + 4
    #               = 3(i^2 + 2i + 1)
    #               = 3(i(i + 2) + 1)
    #               = 3i(i+2) + 3

