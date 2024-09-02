
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # for word in string:
    #     word = int(word)
    #     if word == 2:
    #         return True
    #     elif word == 3:
    #         return True
    #     elif word == 5:
    #         return True
    #     elif word == 7:
    #         return True
    #     elif word % 2 == 0:
    #         return False
    #     elif word % 3 == 0:
    #         return False
    #     elif word % 5 == 0:
    #         return False
    #     elif word % 7 == 0:
    #         return False
    #     else:
    #         return True

    for word in string:
        word = int(word)
        if word <= 2:
            return False
        else:
            for i in range(2, word):
                if word % i == 0:
                    return False
            else:
                return True
