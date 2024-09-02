
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Write your code here
    # Note: You should handle the case when the string is empty or '1'
    for i in range(2, len(string)):
        if string[i] == '1':
            continue
        for j in range(i + 1, len(string)):
            if string[j] == '1':
                continue
            if string[i] % string[j] == 0:
                return False
        return True