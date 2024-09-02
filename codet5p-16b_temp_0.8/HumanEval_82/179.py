
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    num = 0
    for letter in string:
        num += 1
    if num == 2:
        return True
    if num == 1:
        return False
    return prime_length_helper(num)
