
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Your code here
    max_value = 100
    for value in range(2, max_value + 1):
        if string[0] == '1':
            if string[1:] == str(value):
                return True
        elif string[0] != '1':
            if all(val == string[i] for i in range(1, len(string)) for val in str(value) for _ in range(len(string))):
                return True
    return False