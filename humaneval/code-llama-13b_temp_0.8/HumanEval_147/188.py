
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
    
    a = [i*i-i+1 for i in range(1, n+1)]
    i, j, k = 0, 0, 0
    result = 0
    while i<n-2:
        while j<n-1 and a[j]%3!=0:
            j+=1
        while k<n and a[k]%3!=0:
            k+=1
        if j<n-1 and k<n and (a[j]+a[k])%3==0:
            result+=1
        i, j, k = i+1, j+1, k+1
    return result
