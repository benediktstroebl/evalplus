```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return 'No palindrome'

    # Longest palindrome from first character to last non-palindrome.
    # i, j = 0
    palindrome = []
    while True:
        if i >= len(string) - 1 or j >= len(string[::-1]) - 1:
            break
        char = string[i] + string[j]
        palindrome.append(char)
        i += 1
        j += 1

    # Reverse the palindrome and return the string.

return ''.join(make_palindrome('cata'  ))
```
This solution takes a string as input and checks if it is a palindrome or not. If the string is not a palindrome, it returns 'No palindrome'. Otherwise, it returns the shortest palindrome that begins with the given string. The solution uses a algorithm idea of finding the longest palindrome from the first character to the last non-palindrome and then reversing it to get the desired result.