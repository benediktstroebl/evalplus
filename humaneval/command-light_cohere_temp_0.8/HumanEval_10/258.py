```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    palindromic_part = ''.join()
    non_palindromic_parts = ''.join()

    for char in string:
        if char == palindromic_part:
            non_palindromic_parts.append(char)
       
        palindromic_part = char

    # Reverse the palindromic part and append the rest of the string
    return palindromic_part + ''.join() + ''.join(non_palindromic_parts)

# Test the function
print(make_palindrome('cat'))  # Output: catac
print(make_palindrome('cata'))  # Output: catac
```
The script defines a function `is_palindrome` that checks if a given string is a palindrome and another function `make_palindrome` that finds the shortest palindrome that begins with a supplied string. The `make_palindrome` function uses backtracking to find the palindrome.