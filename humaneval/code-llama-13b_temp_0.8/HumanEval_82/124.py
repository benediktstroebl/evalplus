
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    def prime(x):
        counter = 2
        while counter < x:
            if x % counter == 0:
                return False
            counter += 1
        return True
    return prime(len(string))
