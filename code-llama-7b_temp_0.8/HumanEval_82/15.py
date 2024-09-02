
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) == 1:
        return True

    prime_number = 2
    while prime_number < len(string):
        prime = True
        for i in range(2, prime_number):
            if prime_number % i == 0:
                prime = False
                break
        if prime:
            prime_number += 1
        else:
            break
    return prime

