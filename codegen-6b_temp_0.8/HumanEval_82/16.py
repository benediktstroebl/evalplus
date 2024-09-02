
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) == 0:
        return True
    else:
        string_array = list(string)
        string_array.sort()
        for i in range(len(string_array) - 1):
            if string_array[i] == string_array[i + 1]:
                return False
        return True
