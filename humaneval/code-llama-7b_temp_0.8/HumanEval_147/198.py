
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
        Find all the positive integers divisible by 3
        and store their array indices in a dict
        iterate over the array to find out triples
        each triple will have two numbers a[i], a[j] and a[k]
        if i < j < k, a[i] + a[j] + a[k] will be divisible by 3
    """
    triples_count = 0
    array = list(range(1, n + 1))
    div3 = dict()
    for i in range(1, n + 1):
        if i % 3 == 0:
            div3[i] = i
    
    for i in range(1, n - 2):
        if i in div3:
            for j in range(i + 1, n - 1):
                if j in div3:
                    for k in range(j + 1, n):
                        if k in div3:
                            print(i, j, k)
                            triples_count += 1
    return triples_count
    

