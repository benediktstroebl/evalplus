
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    list = []
    for i in range(len(string)):
        list.append(string[i])
    if len(list) == 1 or len(list) == 0:
        return True
    for i in range(2,len(list)):
        if (list[0] == list[i]) or (list[-1] == list[i]):
            return False
    return True
    
