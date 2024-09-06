import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    minSum = math.inf # 최소 합을 반환하기 위해서 최대 값으로 설정
    curSum = 0 # 기본적으로 오름차순이라 앞에서부터 더한다.
    for n in nums:
        curSum += n
        if curSum < minSum:
            minSum = curSum
        if curSum >= 0:
            curSum = 0 # 더해서 벗어나면 0으로 초기화
    return minSum
