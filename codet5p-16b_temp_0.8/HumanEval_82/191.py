
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    if string == "":
        return True
    else:
        count = 1
        for i in string:
            count += 1
        if count == 1:
            return False
        else:
            if prime_length(string[1:]) == True:
                return True
            else:
                return False
