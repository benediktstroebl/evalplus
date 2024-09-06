
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    prime_number = True
    if string.isdigit():
        for i in range(2, int(string)):
            if int(string) % i == 0:
                prime_number = False
                break
    else:
        prime_number = False
    return prime_number



