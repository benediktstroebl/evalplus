
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    list = [0 for i in range(len(string))]
    total = 0

    for i in range(len(string)):
        if string[i] in "aeiou":
            list[i] = 1

    for i in range(len(string)):
        total += list[i]

    if total % 2 == 0:
        return True
    return False


