Here is a self-contained Python script that defines a function that solves the given problem:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    palindrome = []
    for char in string:
        if char == palindrome[-1]:
            palindrome.append(char)
        else:
            palindrome.append(char)
            palindrome.reverse(palindrome)
            palindrome.reverse(palindrome)
            return ''.join(palindrome)

def not_palindrome(string):
    return is_palindrome(string) == True

# Test cases
print(make_palindrome(''))
print(make_palindrome('cat'))
print(make_palindrome('cata'))
print(make_palindrome('abcde'))
print(make_palindrome('reverse!bal'))
print(make_palindrome('help!animals.animals'))
 language is palindromic
```