
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    nums = []
    for num in str(num):
        nums.append(int(num))
    even_sum = sum(nums)
    odd_sum = sum(nums[::2])
    return (even_sum, odd_sum)
