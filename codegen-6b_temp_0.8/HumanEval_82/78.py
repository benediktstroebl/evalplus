
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    test = []
    for i in range(2, len(string)):
        if string[i] in string[:i]:
            test.append(False)
        else:
            test.append(True)
    return all(test)

