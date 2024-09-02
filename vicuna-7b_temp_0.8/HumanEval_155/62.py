
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # If the number is zero, return 0 for both the even and odd counts
    if num == 0:
        return (0, 0)
    
    # For positive numbers, check the number modulo 10 and return the digits of the number in reverse order
    digits = str(abs(num))[::-1].split('')
    # If the number is odd, return (1, digits[0])
    if num % 10 == 1:
        return (1, digits[0])
    # For even numbers, check if the next digit is even or odd and return the difference
    elif num % 10 == 0:
        return (0, 1 if num in [2, 4, 6, 8] else -1)
    
    # For negative numbers, check the number modulo 10 and return the digits of the number in reverse order
    digits = str(abs(num))[::-1].split('')
    # If the number is odd, return (-1, digits[0])
    if num % 10 == 1:
        return (-1, digits[0])
    # For even numbers, check if the next digit is even or odd and return the difference
    elif num % 10 == 0:
        return (-1, 1 if num in [2, 4, 6, 8] else -1)
