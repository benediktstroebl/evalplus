
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
    
    string_length = len(string)
    
    for i in range(2, string_length):
        for j in range(i + 1, string_length):
            if (string[i:j] == string[i] * string[j:]) or (string[i:j] == string[j:i] * string[i:j]):
                return False
        if string[i:string_length] == 1 or string[i:string_length] == string[i:string_length] % 2:
            return True
    
    return False

