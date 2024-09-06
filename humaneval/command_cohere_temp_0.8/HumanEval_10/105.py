Here's a Python script with a self-contained function that solves the problem of forming the shortest palindrome:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix.
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[-i:]):
        i -= 1

    # Find the longest non-palindromic prefix before the palindromic suffix.
    j = 0
    while not is_palindrome(string[j:i]):
        j += 1

    # Swap these two parts to construct the shortest palindrome.
    return make_palindrome(string[j:i][::-1] + string[j+1:i-1])
``` 

The function `make_palindrome()` works as follows:
1. If the input string is empty, it returns the string.
2. Otherwise, it searches for the **longest palindromic suffix** in the string. 
3. Next, it searches for the **longest non-palindromic prefix** before the palindromic suffix.
4. Finally, it reconstructs the shortest palindrome by concatenating the reverse of the longest non-palindromic prefix and the string shortened by the lengths of the longest palindromic suffix and non-palindromic prefix.

This approach guarantees that the result is the shortest possible palindrome.

The `is_palindrome` function is reused from the prompt, which seems correct and well-commented.