
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime_list = []
    for i in range(1, len(string)+1):
        if len(string) % i == 0:
            prime_list.append(i)
    return [x for x in prime_list if is_prime(x)]
