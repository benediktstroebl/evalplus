Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]

def make_palindrome(string: str) -> str:
    """ Returns the shortest palindrome string that starts with the input string """
    if is_palindrome(string):
        return string
    # Find the longest palindrome suffix in the input string
    index = len(string) - len(string)[::-1].index(string[::-1])
    # Reverse the part before the palindrome suffix and append it to the input string
    return make_palindrome(string[:index] + string[index:][::-1])
```

This code snippet works by using the is_palindrome() function to check if the input string is a palindrome. If it is, the make_palindrome() function returns the input string as it is already a palindrome. Otherwise, it finds the longest palindrome suffix in the input string using string[::-1].index(string[::-1]) and then reverses and appends it to the inverted input string[:index]. The process continues until the result is a palindrome.