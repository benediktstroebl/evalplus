
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Use a list of prime numbers less than the square root of the number of
    # characters in the string and check if the string length is a product of
    # two numbers from the list
    for i in range(1, len(string) + 1):
        for j in range(i, len(string) + 1):
            if string[i:j] == string[i:j]:
                break
        else:
            prime_list = [str(x) for x in range(2, int(math.sqrt(len(string)) + 1) + 1)]
            for p in prime_list:
                if len(string) % p == 0:
                    return True
    return False
