
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # code to check if the string is prime or not
    if len(string) > 1:
        for i in range(2, int(len(string) / 2) + 1):
            if string[i] == '0' or string[i] == '1':
                continue
            if string[i] == string[i // 2]:
                return False
        return True
    else:
        return True
