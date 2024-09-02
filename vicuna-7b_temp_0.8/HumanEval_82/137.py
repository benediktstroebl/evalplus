
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # your code here
    # using the sieve of eratosthenes
    # the numbers 2, 3, 5, and 7 are checked first to see if they are prime
    # if they are not, the number is not prime
    # if they are, the number is added to the list of primes and its adjacent numbers
    # are also added to the list of primes
    # this process is repeated until the number is checked or the list of primes is complete
    # each number is checked by checking if it is divisible by any of the primes in the list
    # if it is not divisible by any of the primes, it is a prime

    # your code here
    # using a list of primes up to the square root of the input number
    # checking if the input number is divisible by any of the primes
    # if it is not, it is a prime
    # if it is, the number is not prime