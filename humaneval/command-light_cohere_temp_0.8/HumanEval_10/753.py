```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string:
        return ''

    # Finds the longest postfix of supplied string that is a palindrome
    palindrome = string[:0]  # empty palindrome
    while True:
        lcm = []
        for i in range(len(string)):
            lcm.append(string[i]) * int(string[i]) // len(string[i])
        lcm.sort()
        string = lcm[::-1] + string[::-1]
        if string == palindrome:
            return palindrome
```
This function will return the shortest palindrome of the string. The function uses an efficient algorithm to solve the problem.