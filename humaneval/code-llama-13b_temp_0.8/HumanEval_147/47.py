
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
    a = list(map(lambda x: x*(x-1)+1, range(1, n+1)))
    d = dict()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            k = a[j]+a[i]
            if k%3==0 and (a[i]+a[j]//3) in d:
                count += d[a[i]+a[j]//3]
            if k%3 not in d:
                d[k%3] = 1
            else:
                d[k%3] += 1
    return count

