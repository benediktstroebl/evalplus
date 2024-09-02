
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    odd = lambda x: x % 2 != 0
    def hasOdd(num):
        first = odd(num % 10)
        last = odd(num // 10)
        return first and last

    return len([x for x in nums if x > 10 and hasOdd(x)])
