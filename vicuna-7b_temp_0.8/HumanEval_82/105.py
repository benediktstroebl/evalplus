
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Take the input string as a parameter
    string = str(string)
    # Remove any whitespace
    string = string.strip()
    # Convert the string to lowercase
    string = string.lower()
    # Check if the string is empty
    if len(string) == 0:
        return True
    # Initialize an empty list to store prime numbers
    prime_numbers = []
    # Check if the string is a prime number or not
    for char in string:
        if char == '1':
            prime_numbers.append(1)
        elif char == '2':
            prime_numbers.append(2)
        elif char == '3':
            prime_numbers.append(3)
        elif char == '4':
            prime_numbers.append(4)
        elif char == '5':
            prime_numbers.append(5)
        elif char == '6':
            prime_numbers.append(6)
        elif char == '7':
            prime_numbers.append(7)
        elif char == '8':
            prime_numbers.append(8)
        elif char == '9':
            prime_numbers.append(9)
        elif char == '0':
            prime_numbers.append(int(string[0]))
    # Remove any duplicate numbers from the prime_numbers list
    prime_numbers = list(set(prime_numbers))
    # Check if the length of prime_numbers is equal to the length of string
    if len(prime_numbers) != len(string):
        return False
    # Check if any of the prime numbers in the list are divisible by the length of the string
    for prime_number in prime_numbers:
        if prime_number % len(string) == 0:
            return False
    return True
