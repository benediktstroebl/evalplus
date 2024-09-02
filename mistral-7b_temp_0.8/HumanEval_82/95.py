
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    list_of_string = list(string)
    for i in list_of_string:
        if i in 'aeiouAEIOU':
            list_of_string.remove(i)
    if len(list_of_string) % 2 != 0:
        return True
    else:
        return False

