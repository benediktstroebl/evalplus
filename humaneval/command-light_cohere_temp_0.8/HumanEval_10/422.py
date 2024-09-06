```python
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return ''

    # Using a loop and an efficient approach
    # Find the longest palindrome.
    max_len = 0
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            max_len = i
        else:
            break

    # Creating the palindrome string
    palindrome = string[:max_len]
    reversed_char = string[-1]
    palindrome += reversed_char

    return palindrome
```
This code defines a self-contained Python function that solves the given problem. It efficiently finds the particular tests for the problem by passing the 'make_palindrome'' function.