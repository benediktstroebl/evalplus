
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # Write your code here
    # 1. Set up a counter that starts at 0
    # 2. Loop through the elements of nums
    # 3. If the element is greater than 10, check if the first and last digits 
    # are odd by modulus
    # 4. If they are, add 1 to the counter
    # 5. Return the counter value at the end
    count = 0
    for num in nums:
        if num > 10:
            if num % 10 % 2 == 0:
                if num % 100 // 10 % 2 == 0:
                    count += 1
    return count
