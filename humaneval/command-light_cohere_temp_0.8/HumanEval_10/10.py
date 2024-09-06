```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(input_string):
    # Algorithm: Find the longest palindrome starting from the input string
    palindrome = []
    l = 0
    r = 0

    while l < len(input_string) - 1:
        if is_palindrome(input_string[l:r + 1]):
            palindrome.append(input_string[l:r + 1])
            l += 1
        else:
            r += 1

    # Reverse the palindrome and return the string
    reversed_palindrome = ''.join(reversed(palindrome))
    return reversed_palindrome
```
This code defines a function is_palindrome that checks if a given string is a palindrome or not. It then creates another function make_palindrome that takes an input string and returns the shortest palindrome of the string using a simple algorithm. The function works by finding the longest palindrome substring from the input string and then reversing the substring to get the palindrome.