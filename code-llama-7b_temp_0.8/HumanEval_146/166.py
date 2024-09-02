
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
        # check that the digits are odd
        num_str = str(num)
        first_digit = int(num_str[0])
        last_digit = int(num_str[-1])
        if first_digit % 2 == 1 and last_digit % 2 == 1:
            # check that the number is greater than 10
            if num > 10:
                count += 1
    return count

