
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Use the Sieve of Eratosthenes algorithm to check if a number is prime
    # Divisors are stored in the set [2, n-1]
    # The Sieve of Eratosthenes algorithm involves keeping track of two
    # separate arrays, one for prime numbers and another for composite numbers
    # The algorithm is quite efficient, as it only requires O(n) operations
    # to find all prime numbers up to n.
    # The main idea is to use the fact that composite numbers have at least
    # one divisor in the set of the first n prime numbers
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    n = len(string)
    prime_numbers = [True for i in range(2, n+1)]
    composite_numbers = []
    for i in range(2, n+1):
        for j in range(i**2, n+1, i):
            prime_numbers[j] = False
    for num in string:
        if num > 1:
            for i in range(num-1, n+1):
                if prime_numbers[i] == False:
                    composite_numbers.append(i)
    return all(x for x in composite_numbers if x > 1)
