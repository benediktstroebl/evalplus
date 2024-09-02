
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # I have implemented the code below to check if the input string is a prime number
    # But the code is not working properly and I am unable to find the issue.
    # I have also tried to check the sieve of eratosthenes for this
    # I am unable to find the solution
    # Please help me to fix the code
    # I am also open for any other ways to check if a string is a prime number
    # or any other approach to solve the problem

    # Initialize a variable to store the sum of digits of the number
    sum = 0

    # Iterate through the digits of the number
    for digit in string:
        # Add the current digit to the sum
        sum += digit

        # If the sum is divisible by any digit from 2 to the number itself,
        # the number is not prime
        if sum % digit == 0 for digit in range(2, int(sum**0.5) + 1):
            return False

        # If the sum is not divisible by any digit from 2 to the number itself,
        # the number is prime
        else:
            return True