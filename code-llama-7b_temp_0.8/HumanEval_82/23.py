
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    # O(1)
    if len(string) <= 2:
        return False

    # O(1)
    if string == '':
        return False

    # O(N)
    if len(string) in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        return True

    # O(N^2)
    if len(string) in [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27]:
        return False

    # O(N)
    for i in range(2, len(string)):
        if len(string) % i == 0:
            return False

    return True

