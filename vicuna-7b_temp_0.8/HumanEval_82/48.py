
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Check if the string is empty
    if len(string) == 0:
        return True
    # Check if the string is only one character
    if len(string) == 1:
        return False
    # Check if the string is a prime number
    if is_prime(string[1:]):
        return True
    # Check if the string is divisible by 2
    if string[0] == '0' or string[0] == '1':
        return False
    # Check if the string is divisible by 3
    if string[0] == '0' or string[0] == '3':
        return is_prime(string[1:])
    # Check if the string is divisible by 4
    if string[0] == '0' or string[0] == '4':
        return False
    # Check if the string is divisible by 5
    if string[0] == '0' or string[0] == '5':
        return is_prime(string[1:])
    # Check if the string is divisible by 6
    if string[0] == '0' or string[0] == '6':
        return False
    # Check if the string is divisible by 7
    if string[0] == '0' or string[0] == '7':
        return is_prime(string[1:])
    # Check if the string is divisible by 8
    if string[0] == '0' or string[0] == '8':
        return is_prime(string[1:])
    # Check if the string is divisible by 9
    if string[0] == '0' or string[0] == '9':
        return is_prime(string[1:])
    # Check if the string is divisible by 10
    if string[0] == '0' or string[0] == '10':
        return is_prime(string[1:])
    # Check if the string is divisible by 11
    if string[0] == '0' or string[0] == '11':
        return is_prime(string[1:])
    # Check if the
