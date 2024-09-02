
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    if len(nums) == 1:
        return nums[0]
    
    numbers = []
    odds = [1, 3, 5, 7, 9]
    odd = False
    even = False
    last_odd = False
    first_odd = False
    for number in nums:
        if number > 10:
            numbers.append(number)
    
    for number in numbers:
        last_digit = number % 10
        if last_digit in odds:
            last_odd = True
        else:
            last_odd = False

        first_digit = number // 10
        if first_digit in odds:
            first_odd = True
        else:
            first_odd = False

        if first_odd and last_odd:
            odd = True
        else:
            odd = False

        if first_digit % 2 == 0 and last_digit % 2 == 0:
            even = True
        else:
            even = False

        if odd and even:
            return numbers.index(number) + 1
    

    
