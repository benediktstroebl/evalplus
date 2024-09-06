
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

    for x in range(2, len(string) + 1):
        if x not in prime_list:
            prime_list.append(x)

    print(prime_list)

    if len(string) in prime_list:
        return True
    else:
        return False
