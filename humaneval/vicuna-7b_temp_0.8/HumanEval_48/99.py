

def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # Find length of the string
    n = len(text)
    
    # Initialize variables to store the characters in the string
    # We will use these variables to check if the string is a palindrome
    # or if it is not
    before_i = []
    after_i = []
    
    # Check if the string is a palindrome
    for i in range(n/2):
        if text[i] == text[n-i-1]:
            before_i.append(text[i])
        else:
            after_i.append(text[i])
    
    # Check if the number of characters in the 'before_i' list is equal to the number of characters in the 'after_i' list
    if len(before_i) == len(after_i):
        return True
    else:
        return False