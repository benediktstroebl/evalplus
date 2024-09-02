
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Use a list to store the prime numbers that are less than the length of the string
    prime = [True for _ in range(len(string))]
    prime[:1] = [False]
    for i in range(2, len(string)):
        for j in range(i + 1, len(string)):
            if string[i:j] == string[j:i]:
                prime[j] = False
                break
    # Check if the length of the string is prime
    if len(string) > 2:
        for i in range(2, len(string)):
            if prime[i]:
                if prime[i] != prime[i - 1]:
                    return True
    return False
