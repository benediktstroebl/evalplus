
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        odd_first_odd_last = (num % 1 == 0 and num % 3 == 0 and num % 5 == 0) and (num % 1 == 1 or num % 3 == 1 or num % 5 == 1)
        if odd_first_odd_last:
            count += 1
    return count
