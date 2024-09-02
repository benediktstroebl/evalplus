
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    # your code here
    strlen = len(string)

    if strlen <= 1:
        return False

    for i in range(2, strlen):
        if strlen % i == 0:
            return False
    return True

    # other solution
    # return string and all(map(lambda x: string % x, range(2, string)))
