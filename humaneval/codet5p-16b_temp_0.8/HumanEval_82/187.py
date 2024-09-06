
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    try:
        if len(string) in [0, 1]:
            return True
        else:
            prime = False
            for i in range(1, len(string) + 1):
                if (len(string) % i == 0) and (i in [1, len(string)]):
                    prime = True
                elif (len(string) % i!= 0) and (i not in [1, len(string)]):
                    prime = True
                else:
                    prime = False
                    break
            return prime
    except TypeError:
        return 'Please enter a string!'

