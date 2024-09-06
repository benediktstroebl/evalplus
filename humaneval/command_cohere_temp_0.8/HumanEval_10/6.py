Here's a Python script with a self-contained function that solves the problem using the given `is_palindrome` function:
```python
def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string."""
    # Check if the input string is a palindrome itself
    if is_palindrome(string):
        return string
    
    # Find the longest palindromic suffix in the string
    palindromic_suffix = find_longest_palindromic_suffix(string)
    
    # Reverse the string up to the length of the palindromic suffix,
    # and append it to the front of the string to create a palindrome.
    return palindromic_suffix[::-1] + string[:-len(palindromic_suffix)]

def find_longest_palindromic_suffix(string: str) -> str:
    """Find the longest palindromic suffix of a string."""
    longest_palindromic_suffix = ''
    for i in range(1, len(string) + 1):
        palindromic = string[-i:]
        if is_palindrome(palindromic):
            longest_palindromic_suffix = palindromic
    return longest_palindromic_suffix
``` 

The `make_palindrome` function first checks if the input string is already a palindrome. If it is, it returns the string as it is. Otherwise, it finds the longest palindromic suffix of the string using the `find_longest_palindromic_suffix` function. It then reverses the suffix and appends it to the beginning of the string to create a palindrome of minimal size.

The `find_longest_palindromic_suffix` function iterates through the string starting from the end and checks each substring of length increasing by 1 if it is a palindrome using the `is_palindrome` function. The longest palindromic substring found is returned.

This code assumes the presence of the `is_palindrome` function, which was provided earlier. You can embed it within a Python script along with the `is_palindrome` function, and it should work correctly for the given input cases.