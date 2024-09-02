
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Replace all non-numeric characters with an empty string
    string = "".join(filter(str.isalpha, string))
    # Convert the string to a list
    list_string = string.split()
    # Create a list of all prime numbers less than the square root of the
    # length of the list_string
    primes = [x for x in range(2, int(list_string[0]+1)**2) if x % 2 == 1]
    for number in list_string:
        # Check if the number is prime
        if number > 1:
            if all(x != int(number) for x in primes):
                return True
    return False
