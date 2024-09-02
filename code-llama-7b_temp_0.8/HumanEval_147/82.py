
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
    N = 9
    n = 1
    a[i] = i*i - i + 1 = 0
    a[j] = j*j - j + 1 = 0
    a[k] = k*k - k + 1 = 0
    
    i * j * k = 3
    (i-1)*(j-1)*(k-1) = 2
    
    a[i] * a[j] * a[k] = 0
    (i-1) * (j-1) * (k-1) = 2
    
    (i-1) * (j-1) * (k-1) = 2
    (i-1) * (j-1) * (k-1) * 3 = 6
    
    (i-1) * (j-1) * (k-1) * 3 = 2
    
    
    (i-1) * (j-1) * (k-1) = 2
    (i-1) * (j-1) * (k-1) * 3 = 6
    
    
    i = 1
    j = 2
    k = 3
    
    a[i] * a[j] * a[k] = (1-1) * (2-1) * (3-1) = 1 * 1 * 2 = 2
    
    
    """
    #return (n - 2) * (n - 1) // 2
    return 0



































