
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    string = string.strip()
    string = string.replace(' ','')
    list_of_char = list(string)
    dict_of_char = dict(zip(list_of_char, [0]*len(list_of_char)))
    if len(string) == 1 or len(string) == 0:
        return False
    elif len(string) == 2:
        return True
    elif len(string)%2 == 1:
        for i in range(1,len(string),2):
            dict_of_char[string[i]] = 1
        if 1 not in dict_of_char.values():
            return True
        else:
            return False
    else:
        for i in range(2,len(string),2):
            dict_of_char[string[i]] = 1
        if 1 not in dict_of_char.values():
            return True
        else:
            return False
