
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    length = len(string)
    if length == 1:
        return False
    elif length == 2:
        return True
    elif length % 2 == 0:
        if length < 3:
            return False
        else:
            count = 0
            for i in range(2, length // 2):
                if length % i == 0:
                    count += 1
            if count == 0:
                return True
            else:
                return False
    else:
        count = 0
        for i in range(2, length // 2):
            if length % i == 0:
                count += 1
        if count == 0:
            return True
        else:
            return False
