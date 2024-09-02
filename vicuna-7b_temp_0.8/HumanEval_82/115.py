
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # you can use the Sieve of Eratosthenes algorithm
    # for a more efficient solution
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    # or use a library such as 'primetest'

    # simple solution using a list
    is_prime = []
    for i in range(2, int(string) + 1):
        if string[i:i+2] == "00":
            is_prime.append(True)
        elif string[i:i+2] != "00":
            is_prime.append(False)
        else:
            is_prime.append(string[i] == "1")
    return all(is_prime)
