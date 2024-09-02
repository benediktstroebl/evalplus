import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    """
    If we try brute forcing, we can think of a solution that involves choosing a 
    starting index and then a range for that index. In other words, we can choose
    a window of a certain size in the array.

    Given an array [2, 3, 4, 1, 2, 4], we need to check all possible windows.

    The maximum size of our window is the number of elements in the array itself.
    We can start our range at 1 and go up to the length of the array.

    The answer is the minimum of these solutions:
    minSubArraySum([2]) == 2
    minSubArraySum([2, 3]) == 5
    minSubArraySum([2, 3, 4]) == 9
    minSubArraySum([2, 3, 4, 1]) == 10
    minSubArraySum([2, 3, 4, 1, 2]) == 12
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 14

    Our solution is going to be in the form of:

    # assuming we're starting at index 0, with a window of size 2
    minSubArraySum([2, 3, 4, 1, 2, 4]) ==
    min(
        sum([2, 3]),
        sum([2, 3, 4]),
        sum([2, 3, 4, 1]),
        sum([2, 3, 4, 1, 2]),
        sum([2, 3, 4, 1, 2, 4])
    )

    """

    # init the solution to be infinity
    solution = math.inf

    # loop through the possible window sizes
    for windowSize in range(1, len(nums) + 1):
        # init the sum of the window to 0
        windowSum = 0

        # loop through each index in the array
        for i in range(len(nums) - windowSize + 1):
            # sum up the window
            for j in range(
