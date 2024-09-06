
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime_num = list()

    for i in range(1, len(string)+1):
        if len(string) % i == 0:
            prime_num.append(i)

    for j in prime_num:
        if prime_num.count(j) == 2:
            return True

    return False

