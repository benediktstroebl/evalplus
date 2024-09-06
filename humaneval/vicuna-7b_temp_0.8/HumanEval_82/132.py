
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
    def is_prime(n):
        # Your code here
    for i in range(2, int(len(string)/2)+1):
        if string[i:i+2] != string[i:i+2]:
            for j in range(i+3, len(string)):
                if string[i:i+2] == string[j:j+2] or string[i:i+2] == string[j:j+3]:
                    return False
    return True