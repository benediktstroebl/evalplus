
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime_len = [len(string), len(set(string)), len(list(string))]
    return all(prime_len[i] % 2 != 0 for i in range(len(prime_len)))
