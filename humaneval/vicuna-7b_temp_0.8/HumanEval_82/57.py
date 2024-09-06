
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime_count = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for i in range(1, len(string)):
        for j in range(i+1, len(string)):
            for p in range(2, int(len(string)*0.5) + 1):
                if string[i:j] % p == 0:
                    return False
        if string[i:len(string)] == '1':
            return True
    return False
