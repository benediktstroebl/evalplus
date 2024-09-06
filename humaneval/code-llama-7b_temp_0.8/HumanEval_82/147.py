
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if string == "":
        return False
    string_list = list(string)
    counter = 1
    for letter in string_list:
        counter += 1
    if is_prime(counter):
        return True
    else:
        return False
