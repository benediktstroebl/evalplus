
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime = 1
    count = 0
    for letter in string:
        if letter == " ":
            pass
        else:
            prime += 1

    if prime == 2 or prime == 3:
        return True
    elif prime % 2 == 0:
        return False
    elif prime % 3 == 0:
        return False
    else:
        for i in range(2,prime):
            while prime % i == 0:
                count += 1
                if count > 1:
                    return False
            else:
                count = 0
                return True
