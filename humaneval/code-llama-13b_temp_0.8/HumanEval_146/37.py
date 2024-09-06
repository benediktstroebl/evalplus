
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def check(number):
        """Checks if a number is special.
        A special number is greater than 10 and both first and last digits are odd.
        """
        if number > 10:
            strNumber = str(number)
            if int(strNumber[0]) % 2 != 0 and int(strNumber[-1]) % 2 != 0:
                return True
        return False
    
    count = 0
    for number in nums:
        if check(number):
            count += 1
    return count
    
