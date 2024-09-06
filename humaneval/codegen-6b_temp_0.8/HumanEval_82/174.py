
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # for _ in range(int(math.sqrt(len(string)))):
    #     for i in range(2, len(string)):
    #         if is_prime(i) and len(string) % i == 0:
    #             return False
    # return True

    return all(is_prime(i) and len(string) % i == 0 for i in range(2, len(string)))

