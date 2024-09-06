
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # should use math.prod([False if x % y != 0 for x in a])
    count = 0
    for s in string:
        if s == ' ':
            count = count + 1
    if len(string) % 2 != 0:
        count = count + 1
    if np.prod([False if x % y != 0 for x in string]) != 1:
        return False
    else:
        return True
