
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime_count = 0
    for i in range(1, len(string)):
        for j in range(i+1, len(string)):
            if (string[i:j] == '1' or string[i:j] == '3' or string[i:j] == '7' or string[i:j] == '9') and string[i:j] not in [string[i:j-1], string[i+1:j]]:
                prime_count += 1
    return prime_count == 2
