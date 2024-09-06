
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    def is_prime(n, k):
        if n < 2:
            return False
        if n == 2:
            return True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    string = str(string)
    for i in range(2, len(string) + 1):
        if string[i:i+2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            continue
        for j in range(i+1, len(string)):
            if is_prime(int(string[i:j+1]), j-i+1):
                return True
        return False
    return True
