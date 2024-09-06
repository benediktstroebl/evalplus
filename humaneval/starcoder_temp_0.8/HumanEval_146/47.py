
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # Initialize a variable that will count the number of special numbers.
    special_num = 0

    # Iterate over the given array.
    for num in nums:
        # Get the absolute value of the number and convert it to a string.
        num_str = str(abs(num))

        # Check if the first and last digit are odd.
        if num_str[0] % 2!= 0 or num_str[-1] % 2!= 0:
            # Check if the number is greater than 10.
            if num > 10:
                # Increment the number of special numbers.
                special_num += 1

    # Return the number of special numbers.
    return special_num

