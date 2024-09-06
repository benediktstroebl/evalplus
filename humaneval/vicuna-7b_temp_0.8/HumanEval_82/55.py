
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
        # if n < 2, it is not a prime
        if n < 2:
            return False
        # if n == 2, it is a prime
        if n == 2:
            return True
        # for all other values of n,
        # if n is odd, then it is a prime
        if n % 2 == 0:
            return False
        # if n is even, then it is not a prime
        return True

    for char in string:
        if is_prime(int(char)):
            return True
    return False

string = input("Enter a string: ")
result = prime_length(string)
