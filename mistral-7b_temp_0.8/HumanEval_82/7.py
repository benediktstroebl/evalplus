
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """


    lst = list(string)
    prime = True

    for i in range(2, len(lst)//2+1):
        if len(lst) % i == 0:
            prime = False
            break
    return prime
