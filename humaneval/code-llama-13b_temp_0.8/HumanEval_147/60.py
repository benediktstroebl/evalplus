
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
    
    # a[i] = i * i - i + 1
    # a[i] = i^2 - i + 1
    
    # a[i] + a[j] + a[k] = (i^2 - i + 1) + (j^2 - j + 1) + (k^2 - k + 1)
    #                     = 3 * (i + j + k) - (i + j + k) + 3
    #                     = 3 * (i + j + k)
    
    # So, if (i + j + k) is a multiple of 3
    # then a[i] + a[j] + a[k] is a multiple of 3
    
    # The largest multiple of 3 that is less than or equal to n 
    # is (n // 3) * 3. So we need to check for all (i + j + k) 
    # such that 2 <= i < j < k <= (n // 3) * 3.
    
    # To make (i + j + k) as small as possible, we have to choose the 
    # largest possible values for i and j, and the smallest possible 
    # value for k. So, we should choose i = n - 2, j = n - 1, and 
    # k = (n // 3) * 3.
    
    # Now, we have to check if (i * i - i + 1) + (j * j - j + 1) + ((n // 3) * 3)^2 - ((n // 3) * 3) + 1 is a multiple of 3 or not.
    # If it is, return (i + 1) * (j + 1) * (k + 1)
    # If not, return 0
    
    total_sum = 0
    
    # This is the largest multiple of 3 that is less than or equal to n.
    largest_multiple_of_3 = (n // 3) * 3
    
    # Check if (i * i - i + 1) + (j * j - j + 
