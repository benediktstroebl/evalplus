
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Your code here
    prime_count = 0
    for i in range(2, int(string) ** 0.5):
        if string % i == 0:
            return False
        if string > i:
            prime_count += 1
    return True
