
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    return sum(1 for e in nums if e > 10 and not ((str(e)[0]).isdigit() and (str(e)[-1]).isdigit() and (
        ((str(e)[0]).isdigit() and (str(e)[-1]).isdigit() and (int(str(e)[0]) % 2 == 1)) or ((str(e)[-1]).isdigit() and (
            int(str(e)[-1]) % 2 == 1)))) and not ((str(e)[0]).isdigit() and (str(e)[-1]).isdigit() and (
            ((str(e)[0]).isdigit() and (str(e)[-1]).isdigit() and (
                (int(str(e)[0]) % 2 == 0) and (int(str(e)[-1]) % 2 == 0))))))
