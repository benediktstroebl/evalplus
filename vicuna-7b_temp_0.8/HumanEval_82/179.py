
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for num in prime_list:
        if string[0] == '2':
            if string == '2':
                return True
        if string[0] == '3':
            if string[1] == '3':
                return True
        for i in range(2, len(string)):
            if string[i:i+2] in prime_list:
                return True
    return False
