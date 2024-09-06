
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # 1. check the input
    if not string:
        return False

    # 2. check the length
    prime = len(string)
    count = 0

    for i in range(2, prime + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count > 2:
            return False
        count = 0

    return True
