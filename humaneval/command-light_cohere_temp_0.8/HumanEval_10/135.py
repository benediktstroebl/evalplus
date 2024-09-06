```python
def is_palindrome(string: str) -> bool:
    """ Check if the given string is a palindrome. Return True if it Palindrome, False otherwise """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Convert the string to lowercase
    Find the longest palindrome in the string
    Find the index and length of the palindrome
    Remove the palindrome and reverse the prefix
    Append the reversed prefix to the end of the string
    Convert the string to uppercase
    Return the modified string
    """
    # convert to lowercase
    string = string.lower()
    
    # find_palindrome(string, 0, len(string)-1)
    return string

def find_palindrome(string: str, start: int, end: int) -> int:
    """ Find the length of the longest palindrome in the string [start, end]
    Return the length of the palindrome
    """
    while start < end:
        if string[start] == string[end]:
            start += 1
        else:
            end -= 1
    return end - start + 1

# Test the functions
print(is_palindrome('racecar')) # True
print(make_palindrome('racecar'))  # racecar
print(find_palindrome('racecar', 0, 5))  # 3
```