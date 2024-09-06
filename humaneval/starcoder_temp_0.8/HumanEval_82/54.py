
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    string = string.lower()
    string = string.replace(' ', '')
    string_list = list(string)
    string_length = len(string_list)
    string_list.sort()
    for index in range(len(string_list)-1):
        if string_list[index] == string_list[index+1]:
            return False
    if string_length == 0:
        return False
    if string_length == 1:
        return True
    for index in range(2, string_length+1):
        if string_length % index == 0:
            return False
    return True
