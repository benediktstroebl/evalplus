
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # A prime number is defined as a number greater than 1 that has no
    # positive divisors other than 1 and itself.
    # We can use a sieve array to quickly test if a number is prime.
    # The sieve array is an array of booleans where we set the boolean
    # to True for the numbers that are not prime.
    # We start with the array all set to False, then set the array
    # for the numbers 2 to the square root of the number of elements
    # in the array.
    n = len(string)
    sieve = [True for i in range(1, n + 1)]
    sieve[2] = True
    for i in range(3, int(n ** 0.5) + 1):
        sieve[i] = True
    # Iterate through the string and check if it is prime.
    for i in range(2, int(n ** 0.5) + 1):
        if string[i] == '0' or string[i] == '1' or string[i] in sieve:
            return False
    return True