
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime_count = 2
    current_len = len(string)
    for i in range(2, current_len):
        if string[i] == '1':
            prime_count += 1
        elif string[i] == '0':
            if prime_count % 2 == 0:
                prime_count += 1
            else:
                prime_count = 1
        elif string[i] == '9':
            if prime_count % 3 == 0:
                prime_count += 1
            else:
                prime_count = 1
    if prime_count % 2 != 0:
        return True
    else:
        return False