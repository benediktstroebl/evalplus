
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

    # first, check for the first and last digit. Then, check if the number is bigger than 10
    def checkFirstAndLast(num):
        if (num // 10) % 2 != 0 and (num % 10) % 2 != 0:
            return num % 100 > 10
        return False

    return len(list(filter(checkFirstAndLast, nums)))

