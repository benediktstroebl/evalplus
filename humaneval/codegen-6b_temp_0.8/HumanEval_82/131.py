
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    length = len(string)
    if length < 3 :
        return True
    if length%2 == 0 or length%3 == 0:
        return False
    for i in range(5, int(length**.5)+1, 6): #all prime numbers
        if string[i-1:i+1] == "":
            continue
        for j in range(i, int(length**.5)+1, i):
            if string[j-1:j+1] == "":
                continue
            if length%j == 0 and length%(j*i) == 0:
                return False
    return True
