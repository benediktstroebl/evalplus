Here is a Python script with a self-contained function that solves the problem of finding the shortest palindrome:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    # Function to construct the shortest palindrome
    # from a given string
    longest_palindrome = []
    # Check for the presence of a palindrome and store its length
    l = 0
    r = len(string) // 2
    while l < r:
        if is_palindrome(string[l:r + 1]) == True:
            longest_palindrome.append(string[l:r + 1])
            l += 1
            r -= 1
        else:
            longest_palindrome.append(string[l:r])
            l += 1
            r -= 2
    # Reverse the entire prefix and append to the palindrome
    reverse_prefix = ''.joinstring[::-1]
    # Append the reverse of the prefix and concatenate
    palindrome = ''.joinstring[:0] + ''.join_ palindrome + reverse_prefix
    return palindrome
```
This function, `make_palindrome`, takes a string as input and returns a new string with the shortest palindrome appended to it. The algorithm works by first finding the longest postfix of the input string that is a palindrome. It then appends the the end of the string reverse of a string prefix that comes before the palindromic suffix. Finally, the function concatenates the palindrome with the reverse of the prefix and returns the result.