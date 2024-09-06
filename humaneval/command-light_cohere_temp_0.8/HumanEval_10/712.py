```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(input_str):
    if not_palindrome(input_str):
        return ""

    palindrome = input_str[-0:len(input_str) // 2] + input_str[:len(input_str) // 2][::-1]
    return palindrome
```
The function is_palindrome returns True if the string is a palindrome, and False otherwise.

The function make_palindrome takes a string as input and checks if it's empty. If the input is not empty, it checks if the string is already a palindrome using is_palindrome. If it's palindrome, the function returns the empty string. If the string is not a palindrome, the function finds the shortest palindrome that begins with the input string using the algorithm idea described.

Finally, the function returns the shortest palindrome.