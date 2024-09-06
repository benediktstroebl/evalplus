
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    first_digit_odd = lambda x: x % 10 in [1, 3, 5, 7, 9]
    last_digit_odd = lambda x: (x // 10) % 10 in [1, 3, 5, 7, 9]
    greater_than_10 = lambda x: x > 10
    conditions = (first_digit_odd, last_digit_odd, greater_than_10)
    nums = list(filter(lambda x: all(condition(x) for condition in conditions), nums))
    return len(nums)

