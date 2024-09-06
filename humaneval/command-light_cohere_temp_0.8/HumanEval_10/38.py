```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string): 
    if not_palindrome(string):
        return string + string[::-1]
    return make_palindrome(string[::-1])  # recursive call

def test_make_palindrome(string): 
    return make_palindrome(string) == string + string[::-1] 

# Example usage
print(is_palindrome("")) # False
print(is_palindrome("cats")) # True
print(make_palindrome("")) # ""
print(make_palindrome("cats")) # "cats"
print(test_make_palindrome("")) # True
```
This code provides a solution to the problem of checking if a given string is a palindrome and then constructing the shortest palindrome using the recursive function make_palindrome().