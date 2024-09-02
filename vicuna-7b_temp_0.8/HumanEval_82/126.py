
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

    string = str(string)
    for char in string:
        if char.isdigit() == False:
            for i in range(len(string)):
                if string[i:i+2] == string[i+1:i+3]:
                    if len(string) % 2 != 0:
                        return False
                    if is_prime(int(string[0:i+1])) == False:
                        return False
                    if is_prime(int(string[i+2:])) == False:
                        return False
                    break
    return True
