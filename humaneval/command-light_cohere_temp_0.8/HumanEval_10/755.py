```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea: 
    - Find the longest postfix of supplied string that is a palindrome. 
    - Append to theend of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    def longest_palindrom(string):
        # Find the index of the first palindrome in the string
        idx = 0
        for j in range(1, len(string)):
            if string[j] == string[idx] * string[idx]:
                idx = j
                break

        # Extract the longest palindrome
        return string[:idx] + string[-idx:]

    return longest_palindrome(string)
```