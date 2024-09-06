
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    if string.__len__() == 1:
        return True
    else:
        for i in range(2, int(string.__len__()/2)+1):
            if string.__len__() % i == 0:
                return False
        return True

