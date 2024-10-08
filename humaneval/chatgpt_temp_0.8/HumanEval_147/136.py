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
    a = [i*i - i + 1 for i in range(1, n+1)]  # create the integer array a
    count = 0  # initialize the count of valid triples to 0
    for i in range(n-2):  # iterate through all possible i values
        for j in range(i+1, n-1):  # iterate through all possible j values
            for k in range(j+1, n):  # iterate through all possible k values
                if (a[i]+a[j]+a[k]) % 3 == 0:  # check if sum is divisible by 3
                    count += 1  # increment count if valid triple found
    return count  # return the count of valid triples
