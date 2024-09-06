
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    def is_prime(num):
        if num <= 1:
            return False
        elif num <= 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False

        i = 5

        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False

            i += 6

        return True

    if is_prime(len(string)):
        return True
    else:
        return False

