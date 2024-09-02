
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # check if the string is empty
    if len(string) == 0:
        return True
    
    # check if the string is a prime number
    if len(string) == 1:
        return True
    
    # check if the string is '2'
    if string == '2':
        return True
    
    # check if the string is composed of only digits
    if all(c.isdigit() for c in string):
        return True
    
    # check if the string is a palindrome
    if string == string[::-1]:
        return True
    
    # check if the string is a Fibonacci number
    if any(str(int(c)) == str(int(c) + int(c) + 1) in string for c in Fibonacci):
        return True
    
    return False