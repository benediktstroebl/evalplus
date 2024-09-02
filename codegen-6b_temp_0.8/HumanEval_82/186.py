
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    for index in range(2, len(string)):
        if string[index] == ' ':
            string = string[0:index] + string[index + 1:]
    return len(string) in prime_list

