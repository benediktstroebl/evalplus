
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Define the maximum length of the string
    max_length = 20

    # Define an empty list to store the prime numbers
    prime_numbers = []

    # Define a variable to store the length of the string
    string_length = len(string)

    # If the string length is less than the maximum length
    if string_length < max_length:
        return False

    # Keep iterating through the string until we find a prime number or the
    # string length equals the maximum length
    for i in range(2, string_length + 1):

        # Keep checking if the number is prime by checking if it has any
        # divisors less than or equal to itself
        for j in range(2, i):
            if not j % i == 0:
                prime_numbers.append(i)

    # If all the numbers from 2 to the length of the string have no divisors
    # less than or equal to themselves, then the string length is prime
    return all(not j % i == 0 for j in range(2, string_length + 1) for i in prime_numbers)