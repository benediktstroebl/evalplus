
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    string = string.replace(" ", "")
    prime = False
    if string == "":
        prime = True
    else:
        length = len(string)
        if length > 1:
            for i in range(2, length):
                if length % i == 0:
                    prime = False
                    break
                else:
                    prime = True
        else:
            prime = False

    return prime




