
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
    # You can use a list of known prime numbers and check if the length is in that list
    # If not, you can use the Sieve of Eratosthenes algorithm to check if the number is prime
    # This algorithm is an efficient way to check if a number is prime or not
    # Example:
    # for i in range(2,int(math.sqrt(n))+1):
    #     if n % i == 0:
    #         print n, "is not prime"
    #         return False
    # else:
    #     print n, "is prime"
    #     return True