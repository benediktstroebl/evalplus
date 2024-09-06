Here is a Python script with a self-contained function that solves the problem of finding the longest palindromic subsequence in a given string:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    palindrome = string[:0]
    reversed_prefix = string[::-1][::-1]
    while palindrome[-1] == reversed_prefix[-1]:
        palindrome = palindrome + reversed_prefix[:-1]
        reversed_prefix = reversed_prefix[1:]
        
    return palindrome
```

This code defines a function 'make_palindrome' that takes a string as input and creates the longest palindromic subsequence in the string. The function uses the basic algorithm to find the palindrome: It first checks if the input string is already a palindrome. If it is, the function returns the empty string. Otherwise, it iterates through the string to find the longest palindromic subsequence and appends it to the 'palindrome' variable. The function then checks if the prefix of the 'palindrome' is equal to the reverse of the 'prefix'. Finally, the function returns the 'palindrome'.