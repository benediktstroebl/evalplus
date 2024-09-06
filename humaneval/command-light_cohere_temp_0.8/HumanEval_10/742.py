```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(input_str):
    if not_palindrome(input_str):
        return ""

    palindrome = ""
    while True:
        char = input_str[0]
        input_str = input_str[1:]
        if is_palindrome(char):
            palindrome = char + palindrome[::-1]
        else:
            break

    return palindrome
```
Do you have any further questions about writing clean and efficient code?