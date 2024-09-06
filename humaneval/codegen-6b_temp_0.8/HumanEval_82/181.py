
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    index = 0

    for i in string:
        index += 1
        if index > int(len(string) / 2):
            return False
        if index == int(len(string) / 2):
            return True
        if (string[index - 1] != string[index] and
           string[index - 1] != string[index + 1]):
            return True

