
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    from math import sqrt
    from itertools import count, islice
    return not any(string[i] == string[j] for i in range(len(string) - 1)
        for j in islice(count(i + 1), int(sqrt(len(string)))))
