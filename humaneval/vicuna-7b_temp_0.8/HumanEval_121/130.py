
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    nums = [int(n) for n in lst]
    n = max(lst)
    for i in range(1, len(nums)):
        if (nums[i] % 2) != 0 and (nums[i-1] != nums[i]-1) and nums[i] > n:
            return nums[i-1] + nums[i]
    return 0
