
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    odd_nums = []
    for num in nums:
        if num > 10:
            odd_nums.append(num)
    
    odd_filtered = []
    for num in odd_nums:
        last_digit = num % 10
        first_digit = int(num / 10)
        if (last_digit % 2 == 1 and first_digit % 2 == 1):
            odd_filtered.append(num)
    
    return len(odd_filtered)
    

