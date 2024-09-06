
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Write your solution here:
    while string:
        if string == '':
            return True
        current_char = string[0]
        string = string[1:]
        if current_char != string[0]:
            return False
        string = string[1:]
    return True

