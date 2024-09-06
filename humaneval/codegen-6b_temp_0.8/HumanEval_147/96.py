
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
    def multiple_of_three(nums):
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] % 3 == 0:
                        count += 1
        return count

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return multiple_of_three(get_max_triples(n - 1)) + get_max_triples(n - 2)

