
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    if string == None:
        return False
    if len(string) == 0:
        return True
    if len(string) == 1:
        return True
    if len(string) > 1:
        counter = 0
        for i in range(0, len(string)):
            if i+1 < len(string):
                if string[i]!= string[i+1]:
                    counter += 1
        if counter == 1:
            return True
        else:
            return False



