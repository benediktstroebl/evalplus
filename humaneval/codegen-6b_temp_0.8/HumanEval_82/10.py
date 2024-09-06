
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    return True if len(string) == int(math.pow(len(string),0.5))**2 else False

try:
    import math
except ImportError:
    print('You do not have math. pow is the square function. You are one step closer to becoming a math student!!!')
    print('The square root of a number is the number which can be expressed as the quotient of two integers:')
    print('(3) = 3/2 = 1 + 1/2 = 1.5')
    print('The square root of a number is the number which can be expressed as the quotient of two integers:')
    print('(12) = 4/2 = 2 + 2/2 = 3')
    print('The square root of a number is the number which can be expressed as the quotient of two integers:')
    print('(13) = 5/2 = 2 + 3/2 = 4')
