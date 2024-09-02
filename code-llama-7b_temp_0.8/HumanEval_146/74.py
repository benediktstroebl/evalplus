
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    odd_numbers = [1,3,5,7,9]
    count = 0
    for n in nums:
        if n < 10 and n > -10:
            continue
        first, last = abs(n) % 10, abs(n) / 10
        if first in odd_numbers and last in odd_numbers:
            count += 1
    return count
