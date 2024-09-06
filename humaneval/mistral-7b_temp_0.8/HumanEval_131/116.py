
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    nums = []
    n = str(n)
    for i in range(len(n)):
        if int(n[i]) % 2 == 1:
            nums.append(n[i])
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return int(nums[0])
    else:
        return int(''.join(nums))

