```python
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return 'No palindrome found'
    return ''.join() + string[::-1]
```
The algorithm works by:
1. string first, check if the string is empty or not. If it is empty, return 'No palindrome found'.
2. If the string is not empty, reverse it. Then, append the string reversed prefix to the string.
3. Find the longest postfix of the string that is a palindrome. 
4. Then, remove all characters in the prefix except the palindrome. Append the rest of the string to the end of the string. 
5. Finally, return the string with the palindrome appended.