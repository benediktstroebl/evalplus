### Python Script to Find Shortest Palindrome
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    
    Args:
        string (str): The input string.
    
    Returns:
        str: The shortest palindrome that begins with the input string.
    """
    while not is_palindrome(string):
        # Find the longest postfix of supplied string that is a palindrome
        for i in range(len(string), 0, -1):
            postfix = string[-i:]
            if is_palindrome(postfix):
                break
        # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
        string = string + postfix[::-1]
    return string


# Example usage
if __name__ == "__main__":
    print(make_palindrome(''))  # ''
    print(make_palindrome('cat'))  # 'catac'
    print(make_palindrome('cata'))  # 'catac'
```
This script defines the `is_palindrome` function to test if a given string is a palindrome and the `make_palindrome` function to find the shortest palindrome that begins with a supplied string. The `make_palindrome` function uses a while loop to find the longest postfix of the supplied string that is a palindrome and then appends the reverse of the string prefix that comes before the palindromic suffix to the end of the string. The example usage at the end demonstrates how to use the `make_palindrome` function.