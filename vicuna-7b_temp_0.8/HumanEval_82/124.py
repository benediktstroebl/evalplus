
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # If the string is empty or contains only spaces, return False
    if not string:
        return False

    # If the string is a digit, it's not prime
    if string.isdigit():
        return False

    # For each character in the string
    for char in string:
        # If the character is 2, 3, 4, 5, 6, 7, 8, 9, or 0
        if char in (2, 3, 4, 5, 6, 7, 8, 9, 0):
            # Multiply the number of digits by the number of times the character appears
            # in the string and add 1
            num_digits = len(str(int(string)))
            num_chars = len(string)
            num_chars_2 = 0
            for i in range(len(string)):
                if string[i] == '2':
                    num_chars_2 += 1
            num_chars_2 = int(num_chars_2)
            if num_digits * num_chars_2 > 1:
                return True
        # If the character is not a digit, it's not prime
        elif char != int(string):
            return False

    return True