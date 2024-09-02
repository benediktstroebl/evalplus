
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
    1. 
        Do i = 1 to n
            Do j = i + 1 to n
                Do k = j + 1 to n
                    If a[i] + a[j] + a[k] is multiple of 3
                        count = count + 1
                Done
            Done
        Done

    Runtime: 52 ms, faster than 52.21% of Python3 online submissions for Maximum Number of Ones That Can be Put in an Array with Concatenation.
    Memory Usage: 14 MB, less than 94.57% of Python3 online submissions for Maximum Number of Ones That Can be Put in an Array with Concatenation.
    """
    # print("n=", n)
    # a = [i * i - i + 1 for i in range(1, n + 1)]
    # count = 0
    # for i in range(1, n):
    #     for j in range(i + 1, n + 1):
    #         for k in range(j + 1, n + 1):
    #             if (a[i] + a[j] + a[k]) % 3 == 0:
    #                 count = count + 1
    # return count

    """
    2. 
        Do i = 1 to n
            Do j = i + 1 to n
                Do k = j + 1 to n
                    If a[i] + a[j] + a[k] is multiple of 3
                        count = count + 1
                Done
            Done
        Done

    Runtime: 60 ms, faster than 49.62% of Python3 online submissions for Maximum Number of Ones That Can be Put in an Array with Concatenation.
    Memory Usage: 14 MB, less than 94.57% of Python3 online submissions for Maximum Number of Ones That Can be Put in an Array with Concatenation.
    """
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    
