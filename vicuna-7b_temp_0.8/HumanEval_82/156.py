
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
        if char == " ":
            continue
        if char.isdigit() and len(string) % 2 != 0:
            for i in range(int(char**0.5) + 1):
                if string[i:i+int(char**0.5)] in ['1','0']:
                    if is_prime(int(string[i:i+int(char**0.5)])) == False:
                        return False
        if char.isdigit() and len(string) % 2 == 0:
            for i in range(int(char**0.5) + 1):
                if string[i:i+int(char**0.5)] in ['1','0']:
                    if is_prime(int(string[i:i+int(char**0.5)])) == True:
                        return True
        if char == '!':
            if is_prime(int(string[i+1:])) == True:
                return True
        if char == '%':
            if is_prime(int(string[i+2:])) == True:
                return True
    return True
