
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # Step 1: Declare a variable to store the number of elements that satisfy the 
    # condition and initialize it to 0.
    num_elements = 0
    # Step 2: Loop through the input array and check if each element is greater than 10 
    # and both its first and last digits are odd (1, 3, 5, 7, 9). If the condition is 
    # met, increment the number of elements.
    for num in nums:
        if num > 10:
            if num % 10 % 2 == 1:
                if num // 10 % 10 % 2 == 1:
                    num_elements += 1
    # Step 3: Return the number of elements that satisfy the condition.
    return num_elements
