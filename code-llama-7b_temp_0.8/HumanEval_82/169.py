
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    #replace the following pass statement with your code
    prime_len = [len(string), len(string) - 2, len(string) - 4, len(string) - 6, len(string) - 8]
    prime_num = prime_len[0]

    for i in prime_len:
        if i <= 1:
            prime_num = prime_num + 1
        elif i % 2 == 0 or i % 3 == 0:
            prime_num = prime_num + 1

    if prime_num == 0:
        return True
    else:
        return False
