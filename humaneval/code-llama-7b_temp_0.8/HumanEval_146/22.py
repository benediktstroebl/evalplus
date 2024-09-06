
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    odd_number = []
    number_with_odd_first_and_last_number = []
    for num in nums:
        if num > 10:
            odd_number.append(num)
        if num > 10 and num % 10 in [1, 3, 5, 7, 9] and num // 10 % 2 == 1:
            number_with_odd_first_and_last_number.append(num)
    
    print(odd_number)
    print(number_with_odd_first_and_last_number)
    return len(odd_number) + len(number_with_odd_first_and_last_number)

