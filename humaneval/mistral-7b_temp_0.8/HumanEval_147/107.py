
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
    a = []
    for i in range(1,n+1):
        a.append(i**2 - i + 1)
    sum = a[0] + a[1] + a[2]
    count = 0
    for i in range(len(a)-2):
        if i + 3 <= len(a):
            for j in range(i+1, len(a)-1):
                if j + 2 <= len(a):
                    sum = a[i] + a[j] + a[j+1]
                    if sum % 3 == 0:
                        count += 1
    return count


