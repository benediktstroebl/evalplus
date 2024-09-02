
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    res = 0
    for num in nums:
        if num > 10 and num % 2 != 0 and num % 10 != 5 and num % 10 != 6:
            res += 1
    return res


"""
Function: palindromeOf(str)

Description: A palindrome is a word, phrase, number, abbreviation or other 
            form of a word which reads the same backwards as forwards. The 
            function takes a string as input and returns true if the string 
            is a palindrome, false otherwise.

Example: palindromeOf("madam") => true

"""
