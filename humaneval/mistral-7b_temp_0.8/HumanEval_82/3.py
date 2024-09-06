
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    try:
        list_of_chars = list(string)
        is_prime = True
        for i in range(2, len(list_of_chars) - 1):
            if i == 2:
                continue
            if list_of_chars[i] == list_of_chars[i-1] and list_of_chars[i] == list_of_chars[i+1]:
                is_prime = False
            if list_of_chars[i] == list_of_chars[i+1]:
                is_prime = False
        return is_prime
    except:
        return False

