
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
    # first, create the list of numbers that we will use to find
    # the sum of three consecutive numbers
    nums = []
    for i in range(1, n + 1):
        nums.append(i * i - i + 1)

    # now we loop through the numbers and check if the sum of any 3
    # consecutive numbers is a multiple of 3
    count = 0
    for i in range(2, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if (nums[i] + nums[j] + nums[k]) % 3 == 0:
                    count += 1

    return count

