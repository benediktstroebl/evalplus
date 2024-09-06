Here is a self-contained Python script that solves the problem of finding the shortest palindrome:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return string
    else:
        #Find the longest postfix of supplied string that is a palindrome
        palindrome = string[:string.find(str.r] + str.reverse(str[r)
        to string
        return palindrome

def not_palindrome(string):
    return not is_palindrome(string)

# Testing
print(make_palindrome(''))
print(make_palindrome('cat'))
print(make_palindrome('cata'))
print(make_palindrome('cad'))
print(make_palindrome('racecar'))
print(make_palindrome('very $great palindrome'))
```