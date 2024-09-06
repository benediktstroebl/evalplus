```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    postfix = string[1:] 
    while postfix[-1] != postfix[0]: 
        postfix = postfix[0] + postfix[1:]

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return string[:1] + postfix[::-1] + string[2:]
```
The code defines two functions: is_palindrome checks if a given string is a palindrome, and make_palindrome finds the shortest palindrome that begins with the given string. The function use a string slicing and recursive approach to solve this problem.