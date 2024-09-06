
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    filtered_numbers = []
    for num in nums:
        first_digit = int(str(num)[0])
        last_digit = int(str(num)[-1])
        if num > 10 and first_digit % 2 != 0 and last_digit % 2 != 0:
            filtered_numbers.append(num)
    return len(filtered_numbers)
