
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    prime_list = []

    for x in range(2, len(string)+1):
        if len(string) % x == 0:
            prime_list.append(x)

    if len(prime_list) == 2:
        return True
    else:
        return False
