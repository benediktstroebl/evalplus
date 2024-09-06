
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    """
    <your code goes here>
    """
    n = len(string)
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
        else:
            count += 0
    if count == 2:
        return True
    else:
        return False
