
def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    # Replace all non-alphanumeric characters with "X"
    s = s.translate(str.maketrans("X", "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", "X"))
    
    # Initialize the result
    result = s.lower()
    
    # Iterate over the characters in the string
    for i in range(len(s)):
        # If the character is alphanumeric
        if s[i].isalpha():
            # Uppercase the character if the previous character is lowercase
            if i > 0 and s[i-1].islower():
                result = result[0].upper() + result[1:]
            # Lowercase the character if the previous character is uppercase
            elif i > 0 and s[i-1].isupper():
                result = result[0].lower() + result[1:]
            # Remove the character from the result
            result = result[:i] + result[i+1:]
        
    return result