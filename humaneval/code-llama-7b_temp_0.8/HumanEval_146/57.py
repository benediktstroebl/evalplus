
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

    # Create a list to store filtered numbers
    filtered_nums = []

    # Loop through the array
    for num in nums:
        
        # Check if the number is greater than 10
        if num > 10:

            # Check if the first and last digits are odd
            if num % 10 % 2 != 0 and num // 10 % 2 != 0:
                filtered_nums.append(num)

    return len(filtered_nums)
