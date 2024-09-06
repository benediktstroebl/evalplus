
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
    # Find and return the number of triplets 
    # that have a sum that is a multiple of 3.
    if n < 2:
        return 0
    
    arr = [i * i - i + 1 for i in range(1, n+1)]
    # Make the array cyclic.
    arr.extend(arr[:2])
    
    # Use sliding window technique.
    count = 0
    i = 0
    j = 1
    k = 2
    
    while k <= len(arr):
        # If the current sum is a multiple of 3,
        # then increment the answer by 1.
        if (arr[i] + arr[j] + arr[k]) % 3 == 0:
            count += 1
            
        k += 1
        j += 1
        i += 1
        
        # Move j back to i when j becomes larger than i.
        if j > i:
            j = i
            
        # Move i back to the start when i becomes larger than k - 2.
        if i > k - 2:
            i = k - 2
            
    return count

