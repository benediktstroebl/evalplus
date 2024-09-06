
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # your code here

    # Initialize a counter variable to keep track of the number of elements that match the condition
    count = 0

    # Iterate through the array and check if each element is greater than 10 and both the first and last digits are odd
    for num in nums:
        if num > 10 and (num // 10 % 10) % 2 == 1 and num % 10 % 2 == 1:
            count += 1

    # Return the count
    return count
