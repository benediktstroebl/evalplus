
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    def prime_check(n):
        if n % 2 == 0:
            return False
        else:
            i = 3
            while i < n:
                if n % i == 0:
                    return False
                i += 2
        return True

    if string == "":
        return False
    else:
        return prime_check(len(string))

