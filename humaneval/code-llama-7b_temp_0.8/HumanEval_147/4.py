
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
    # LC: https://leetcode.com/problems/count-triplets-in-an-array-with-sum-equal-to-zero/
    # 
    # Time and Space complexity: O(n^2)
    # -----------------------------------
    # The brute force approach is to use three nested loops to iterate over the array
    # and check if a[i] + a[j] + a[k] is a multiple of 3. Since we have to iterate over
    # n^2 elements, the time complexity will be O(n^2).
    # The space complexity will be O(1) as we are not using any additional space.

    arr = [i * i - i + 1 for i in range(1, n + 1)]
    max_triplets = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (arr[i] + arr[j] + arr[k]) % 3 == 0:
                    max_triplets += 1
    return max_triplets

