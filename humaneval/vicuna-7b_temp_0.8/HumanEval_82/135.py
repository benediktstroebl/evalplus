
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
    i = 2
    while i * i <= len(string):
        if string[i] != '1':
            for j in range(i + 1, len(string)):
                if string[j] == '1':
                    break
                else:
                    return False
        i += 1
    return True
