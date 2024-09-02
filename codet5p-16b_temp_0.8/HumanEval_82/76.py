
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    prime = False
    try:
        if len(string) > 1 and string.isdigit() == True:
            for i in range(2, int(len(string) / 2 + 1)):
                if len(string) % i == 0:
                    prime = False
                    break
                else:
                    prime = True
        else:
            raise ValueError
    except ValueError:
        print('Not a valid input')
    return prime

