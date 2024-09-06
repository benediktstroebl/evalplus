
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    #string = 'string'
    #if len(string) is a prime number

    for i in range(len(string)):
        if i==0:
            continue
        if i==len(string):
            break
        if i%2 != 0:
            continue
        return False
    else:
        return True



    #return True if len(string) is a prime number or False otherwise
