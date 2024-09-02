
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # your code here
    for i in range(2, len(string)):
        for j in range(i + 1, len(string)):
            if string[i:j] == string[i-1:j-1] or (string[i:j] == string[i:j-2] + string[i-1:j-1]):
                return False
        if len(string) % i == 0:
            return True
    return False