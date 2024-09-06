
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def f(n):
        sum = 0
        for i in range(len(n) - 1):
            if n[i] >= 10 and n[i] % 2 == 1 and n[i] % 3 == 1 and n[i+1] % 2 == 1:
                sum += 1
        return sum
    return f(nums)
