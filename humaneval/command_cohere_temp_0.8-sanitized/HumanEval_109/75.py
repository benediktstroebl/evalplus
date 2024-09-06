def move_one_ball(arr):
    nums = list(arr)
    nums.sort()
    if arr == nums or not nums:
        return True
    return False