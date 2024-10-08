
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    lst = []
    for number in nums:
        if number > 10:
            lst.append(number)
    for number in lst:
        if (int(str(number)[0])%2 == 1 and int(str(number)[-1])%2 == 1):
            return lst.count(number)
