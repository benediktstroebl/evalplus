Here is a self-contained Python function that solves the problem:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    # Algorithm idea: Find the longest palindrome using reverse and append.
    longest_palindrome = find_longest_palindrome(string)
    return longest_palindrome + ''.join[::-1]

def find_longest_palindrome(string):
    # Helper function to find the longest palindrome
    return ''.join[::-1].join(string.split()[::-1])
longest_palindrome = ''
```

This function, is_palindrome, returns true if the string is a palindrome and false otherwise. The function, make_palindrome, takes a string and returns the shortest palindrome that begins with the given string. The algorithm idea is to find the longest palindrome using reverse and then append the reverse of a string prefix that comes before the palindromic suffix.