
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime_count = [True for i in range(2, int(string[0] + 1) ** 0.5 + 1)]
    for char in string:
        for i in range(2, int(char + 1) ** 0.5 + 1):
            if char * i <= string[0]:
                for j in range(i, int(string[0] + 1) ** 0.5 + 1, char * (-i % int(string[0] + 1) ** 0.5)):
                    if string[0:j] % i == 0:
                        prime_count[prime_count.index(True)] = False
    return all(prime_count)
