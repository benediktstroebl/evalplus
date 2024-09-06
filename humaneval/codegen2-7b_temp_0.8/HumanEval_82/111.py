
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if not isinstance(string, str):
        raise TypeError("You must give me a string")
    for num in string:
        if num.isalpha():
            return False
        for i in range(2, int(num)):
            if num % i == 0:
                return False
    return True
