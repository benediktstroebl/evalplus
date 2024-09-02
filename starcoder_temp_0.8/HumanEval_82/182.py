
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Your code here
    prime = True
    count = 1
    for letter in string:
        if letter == string[-1]:
            count += 1
        else:
            count += 1
            prime = False
    if count == 2:
        prime = True
    return prime
