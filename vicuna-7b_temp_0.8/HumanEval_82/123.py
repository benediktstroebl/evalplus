
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    def is_prime(n, max_val):
        """
        Check if a number is prime or not
        """
        if n < 2:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_prime(number):
        max_val = 1000000
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def prime_length(string):
        n = int(len(string))
        max_val = 1000000
        for i in range(2, n + 1):
            if check_prime(str(i)) == False:
                return False
        return True

    return prime_length(string)
