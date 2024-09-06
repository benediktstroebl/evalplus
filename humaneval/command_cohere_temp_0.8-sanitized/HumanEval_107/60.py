def is_palindrome(num):
    """
    Helper function to determine if a number is a palindrome.
    Args:
        num (int): Number to be checked
    
    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    return str(num) == str(num)[::-1]
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    Args:
        n (int): Positive integer container expects
    
    Returns:
        tuple: A tuple containing (count of even palindromes, count of odd palindromes)
    """
    even_count, odd_count = 0, 0
    for num in range(1, n+1):
        if is_palindrome(num):
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)