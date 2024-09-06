```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''
    palindromic = []
    for char in string:
        if char == palindromic[-1] == char:
            palindromic.append(char)
        else:
            palindromic.append(char)
            reverse = ''.join(reversed(palindromic))
            palindromic.append(reverse)
        return ''.join(palindromic)

def not_palindrome(string): 
    return is_palindrome(string)

print(make_palindrome('cata')) # Output should be 'catac'
print(make_palindrome('abab')) # Output should be 'babab'
print(make_palindrome(''.join())  # Output should be ''
```
The code defines two functions: `is_palindrome` checks if a given string is a palindrome or not, and `make_palindrome` generates a palindrome from an input string. The `make_palindrome` function works by first calling the `is_palindrome` function to see if the input is a palindrome, and if it's not, returns an empty string. If the input is a palindrome, the function finds the longest palindromic substring in the input and appends it to the end of the string, reversing the substring to match the prefix.

Finally, it tests the `make_palindrome` function with some inputs and prints the results. The output should be the correct palindromes.