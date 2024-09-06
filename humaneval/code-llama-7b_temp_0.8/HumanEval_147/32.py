
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
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    max_triples = 0
    count = 0
    start = 0

    for end in range(1, n + 1):
        while (start < end) and (start * start + start + 1) % 3 != 0:
            start += 1
        end_num = end * end - end + 1
        count = 0

        for i in range(start, end):
            if (i * i + i + 1) % 3 == 0:
                count += 1

        max_triples += count * (count - 1) // 2
        start += 1

    return max_triples

