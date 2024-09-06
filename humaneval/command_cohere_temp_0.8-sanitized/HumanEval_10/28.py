def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    # Find the position of the first non-palindromic character 
    index = string.find(string[::-1], len(string) // 2) + 1
    
    # Reverse the string from index to the end, preserving only the palindromic part 
    palindrome = string[index:] + string[index:][::-1]
    
    return f"{string}{palindrome}"