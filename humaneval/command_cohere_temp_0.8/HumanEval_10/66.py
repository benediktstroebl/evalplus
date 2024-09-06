Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]

def make_palindrome(string: str) -> str:
    """Returns the shortest palindrome string that starts with the input string."""
    if is_palindrome(string):
        return string
    # Find the longest palindromic suffix.
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[-i:]):
        i -= 1
    # Find the longest non-palindromic prefix before the palindromic suffix.
    j = 0
    while not is_palindrome(string[j:i]):
        j += 1
    return make_palindrome(string[:j] + string[i:][::-1])
```

This code defines a function `make_palindrome` that takes a string as input and returns the shortest palindrome string that starts with the input string. The function utilizes the `is_palindrome` function to check if a given string is a palindrome or not.

The function follows the algorithm steps:
1. If the input string is already a palindrome, it's returned as is because it will certainly be part of the generated result.
2. Find the longest palindromic suffix of the input string. This is done by iterating through the string from right to left with `i` and checking if each substring is a palindrome using the `is_palindrome` function. The index `i` is incremented until a non-palindromic substring is encountered.
3. Find the longest non-palindromic prefix before the palindromic suffix. This is done by iterating through the string from left to right with `j` and checking if each substring is not a palindrome. The index `j` is incremented until a palindromic substring is encountered.
4. The make_palindrome function is called recursively with the prefix string preceding the palindromic suffix and the reverse of the suffix appended to the prefix.

This process continues until a palindrome is formed. Since we are working with a prefix of a palindrome and a suffix of a palindrome, the resultant string concatenation of the two parts reversed will be a palindrome. The resultant palindrome is then returned. 

The `make_palindrome` function calls itself recursively and returns the shortest palindrome string that starts with the input string.

Note: The code assumes that the input string contains only letters, and it may not work correctly for strings with other characters. The code also assumes that the input string is non-empty. If the input string is empty, the function returns the empty string.