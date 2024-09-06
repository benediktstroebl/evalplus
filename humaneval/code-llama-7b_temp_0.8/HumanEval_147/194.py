
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
    # edge cases
    if n <= 2:
        return 0
    
    # store the value of a[i] in a hashmap
    mod3 = {}
    count = 0
    max_index = 0
    # we will loop over the array to count the number of times a[i] is a multiple of 3
    for i in range(1, n+1):
        if i * i - i + 1 % 3 == 0:
            mod3[i * i - i + 1] = 1
            max_index += 1

    # print(mod3)
    # we will loop over the array to count the number of times a[i], a[j], a[k] is a triplet
    for i in range(1, n):
        for j in range(i+1, n):
            for k in range(j+1, n+1):
                if (i * i - i + 1) + (j * j - j + 1) + (k * k - k + 1) in mod3:
                    count += 1
    return count
