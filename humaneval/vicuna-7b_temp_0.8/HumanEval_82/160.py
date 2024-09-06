
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # A list of numbers that divide 2, 3, 4
    divisors = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    # A variable to store the length of the current number
    current_length = 0
    # Loop through each character in the string
    for char in string:
        # If the current character is a digit, increment the length and check if it's a prime number
        if char.isdigit():
            current_length += 1
            if current_length == 2:
                # Check if the number is prime
                if not divisors[int(char) - 2] % 2 == 0:
                    return True
            elif current_length > 2:
                # Check if the number is prime
                for i in range(3, current_length + 1):
                    if not divisors[i] % current_length == 0:
                        return True
                return True
        else:
            # Otherwise, we've reached the end of the string
            return True
