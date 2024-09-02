
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

    def cond1(num):
        return num > 10

    def cond2(num):
        return num % 10 % 2 == 1

    def cond3(num):
        return num // 10 % 2 == 1

    return len([x for x in nums if cond1(x) and cond2(x) and cond3(x)])
