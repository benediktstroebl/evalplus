
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # We want to find the length of the string
    # Using the len function
    len_string = len(string)
    # For the function to return true, the length
    # of the string must be a prime number
    # We need to use a for loop
    # with two counters (i and j)
    # This will allow us to iterate over the
    # elements in the string one by one
    # If the length of the string is a prime number
    # The function will return True
    # Otherwise it will return False
    for i in range(2, len_string):
        j = 2
        # If j is less than the length of the string
        # and the string is a prime number
        # The function will return True
        # Otherwise it will return False
        while j < len_string:
            if i % j == 0:
                j += 1
            else:
                break
    if i == len_string:
        return True
    else:
        return False
