
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    if len(string) == 1:
        return True
    else:
        prime_length = True
        for x in range(1,len(string)+1):
            if string[:x] == "":
                continue
            else:
                if prime_length == True:
                    if prime_length == True:
                        if prime_length == True:
                            if prime_length == True:
                                return True
                            else:
                                prime_length = False
                        else:
                            prime_length = False
                    else:
                        prime_length = False
                else:
                    return False
        return False
