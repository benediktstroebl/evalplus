
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
    count = 0
    array = [i * i - i + 1 for i in range(1, n + 1)]
    # For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
    # the last possible value of a[i] is n * n - n + 1 = (n * n - n) / 2 + (n - 1) / 2
    max_value = ((n * n - n) // 2) + ((n - 1) // 2)
    # for each j (j ∈ [1, i - 1])
    for j in range(1, n):
        # for each k (k ∈ [j + 1, i - 1])
        for k in range(j + 1, n):
            # if (a[j] + a[k]) % 3 = 0 and a[j] + a[k] ≤ a[i] and a[j] + a[k] > a[j - 1] + a[k - 1]
            if (array[j] + array[k]) % 3 == 0 and (array[j] + array[k]) <= max_value and (
                array[j] + array[k]) > array[j - 1] + array[k - 1]:
                count += 1

    return count

