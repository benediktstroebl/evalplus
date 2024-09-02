
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Write your code here

    def prime_number(n):
        for i in range(2, int(n / 2) + 1):
            if n % i == 0:
                return False
        return True

    if prime_number(len(string)):
        return True
    else:
        return False


