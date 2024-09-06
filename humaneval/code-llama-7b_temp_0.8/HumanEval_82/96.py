
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    count = 0
    for letter in string:
        count += 1
        # if len(string) is prime return True

    return True if is_prime(count) else False

