```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    lst = []
    for char in string:
        if char == char[::-1]:
            lst.append(char)
    if not lst:
                break
    return ''.join(lst)
```
The make_palindrome function takes a string s as input and checks if it's empty. Then, it iterates through each character in the string to see if it's an identical palindrome, if it is, it appends it to the list lst, and breaks the loop. The list's characters are then reversed and appended to the string at the end to form a palindrome.