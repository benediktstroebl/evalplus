
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # using a dictionary to store prime numbers and checking if the string length is in the dictionary
    # also using the sieve of eratosthenes method to find prime numbers
    prime_count = 2
    for i in range(2, int(string) ** 0.5 + 1):
        if string[i] == '1' or string[i] == '0':
            prime_count = 0
        for j in range(i + 1, len(string)):
            if string[i] == '1' and string[j] == '1':
                prime_count = 0
                break
        if prime_count == 0:
            return True
    return False
