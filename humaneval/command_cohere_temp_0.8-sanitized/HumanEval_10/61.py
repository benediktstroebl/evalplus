def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return string
    
    # Find the longest palindromic postfix and remove it from the string
    i = len(string) - 1
    while i >= 0 and not is_palindrome(string[-i-1:]):
        i -= 1
    string = string[:-i-1]
    
    # Find the shortest palindromic prefix that precedes the above palindromic postfix
    j = 0
    while not is_palindrome(string[:j] + string[-i-1:]):
        j += 1
    
    # Construct the answer by reversing the palindromic prefix and appending it to the string
    answer = string + string[::-1][:j]
    
    return answer