
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def odd(n):
        return n % 2 == 1
    
    def first_last_odd(n):
        first = int(str(n)[0])
        last = int(str(n)[-1])
        return odd(first) and odd(last)
        
    def greater_than_10(n):
        return n > 10

    odds = filter(odd, nums)
    return sum(map(lambda n: first_last_odd(n) and greater_than_10(n), odds))
