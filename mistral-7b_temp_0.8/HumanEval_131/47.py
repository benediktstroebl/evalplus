
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # your code here
    nums = []
    while n:
        nums.append(n%10)
        n = n//10
    products = 1
    for i in range(len(nums)):
        if nums[i] % 2:
            products *= nums[i]
    if len(nums) == 0:
        return 0
    else:
        return products



