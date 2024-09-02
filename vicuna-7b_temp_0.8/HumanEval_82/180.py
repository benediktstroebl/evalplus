
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # your code here
    
    # check for prime numbers up to the square root of the length of the string
    for i in range(int(len(string) ** 0.5)):
        if string[i] == '1':
            continue
        if string[i] == '0':
            if len(string) % 2 == 0:
                continue
        for j in range(i+1, len(string)):
            if string[j] == '1' and string[i] == '1':
                continue
            if string[j] == '0' and string[i] == '0':
                continue
            if string[j] > string[i]:
                break
        else:
            return True
    return False
