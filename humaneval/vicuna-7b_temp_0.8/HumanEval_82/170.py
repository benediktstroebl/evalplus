
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime_count = 0
    for char in string:
        if char == "":
            continue
        if char.isdigit():
            prime_count += 1
    if prime_count == 1:
        return True
    if prime_count >= 2:
        for i in range(2, len(string)):
            if string[i:i+2] == string[i-1:i+2] or string[i:i+2] == string[i+1:i+3]:
                return False
        return True
    return False
