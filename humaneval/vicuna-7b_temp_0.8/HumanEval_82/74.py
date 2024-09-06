
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Test for numbers less than 2
    if len(string) < 2:
        return True
    # Test for palindrome numbers
    if string == string[::-1]:
        return True
    # Test for even numbers
    if string.is_even():
        return False
    # Test for odd numbers
    if not string.is_even():
        return True
    # Test for composite numbers
    for i in range(2, len(string)):
        if string[i] == string[i-2] or string[i] == string[i-1]+string[i-2]:
            return False
    return True
