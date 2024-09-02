
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    lenght = len(string)
    if lenght == 1:
        return False
    if lenght == 2:
        return True
    if lenght % 2 == 0:
        return False
    counter = 3
    while counter <= lenght / 2:
        if lenght % counter == 0:
            return False
        counter += 2
    return True


