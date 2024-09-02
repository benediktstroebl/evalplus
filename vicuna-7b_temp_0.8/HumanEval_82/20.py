
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
    # You can use a prime number check function like this
    # https://www.mathsisfun.com/prime-numbers.html
    # or
    # https://docs.python.org/3/library/math.html#math.isprime
    for num in string:
        if num == 2 or (num > 2 and num % 2 == 0):
            return False
        if (num > 2 and num % 3 == 0):
            return False
        for i in range(4, int(num ** 0.5) + 1, 6):
            if (num % i == 0):
                return False
    return True