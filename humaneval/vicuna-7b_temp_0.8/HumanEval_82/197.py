
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for char in string:
        if char.isdigit():
            n = int(string[:char])
            if is_prime(n) and is_prime(n + str(char)):
                return True
        elif char == 'p' or char == 'P':
            n = int(string[:char])
            if is_prime(n) and is_prime(n + str(char)):
                return True
        elif char == 'p' or char == 'P':
            n = int(string[:char])
            if is_prime(n) and is_prime(n + str(char)):
                return True
        elif char == 'o' or char == 'O':
            n = int(string[:char])
            if is_prime(n) and is_prime(n + str(char)):
                return True
        elif char == 'o' or char == 'O':
            n = int(string[:char])
            if is_prime(n) and is_prime(n + str(char)):
                return True
        elif char == 'd' or char == 'D':
            n = int(string[:char])
            if is_prime(n) and is_prime(n + str(char)):
                return True
        elif char == 'd' or char == 'D':
            n = int(string[:char])
            if is_prime(n) and is_prime(n + str(char)):
                return True
        elif char == 'c' or char == 'C':
            n = int(string[:char])
            if is_prime(n) and is_prime(n + str(char)):
                return True
        elif char == 'c' or char == 'C':
            n = int(string[:char])
            if is_prime(n) and is_prime(n + str(char)):
                return True
        elif char == 'b' or char == 'B':
            n =
