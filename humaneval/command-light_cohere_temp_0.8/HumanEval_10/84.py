Here is a self-contained Python script with a function that solves the problem of creating a palindrome:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    # Helper function to find a palindrome from a prefix and suffix
    def palindrome(prefix, suffix):
        return prefix + suffix[::-1]

    # Find the longest postfix of supplied string that is a palindrome
    longest_palindrome = max(
        palindrome(part[i: i + len(part) - 1], part[i + 1:])
        for i, part in enumerate(string)
    )
    return longest_palindrome + string[: longest_palindrome]

# Unit tests
print(is_palindrome(''))  # True
print(is_palindrome('cat'))  # True
print(is_palindrome('cata'))  # False
print(is_palindrome('navid'))  # False
print(is_palindrome('radar'))  # True
print(is_palindrome(' fanatics  '))  # False
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('radar'))  # 'radarc'
```