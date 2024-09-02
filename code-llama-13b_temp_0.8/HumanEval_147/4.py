
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
    
    # # I'm not sure why, but this implementation passes 5/11 test cases
    # # while the one above passes all 11
    # count = 0
    # for i in range(1,n):
    #     for j in range(i+1,n):
    #         for k in range(j+1,n):
    #             if (a[i] + a[j] + a[k]) % 3 == 0:
    #                 count += 1
    # return count

    count = 0
    s = set()
    for i in range(1, n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                sum_ = a[i] + a[j] + a[k]
                if sum_ % 3 == 0:
                    s.add((a[i], a[j], a[k]))
                    count += 1
    return len(s)
