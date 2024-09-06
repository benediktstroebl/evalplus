
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Make the function more efficient by using a dictionary to store the
    # prime numbers
    prime_numbers = [True for _ in range(1, int(math.sqrt(len(string)) + 1) + 1)]
    for i in range(2, len(string)):
        # If the string has 2 or more characters, the length is not prime
        if len(string) > 1:
            for j in range(2, int(math.sqrt(len(string)) + 1) + 1):
                if string[i] == j:
                    # If the current character is the same as the divisor,
                    # the length is not prime
                    break
                elif prime_numbers[j]:
                    # If the divisor is prime, the length is not prime
                    return False
            # If the divisor is not prime, the length is prime
            prime_numbers[i] = True
    return True