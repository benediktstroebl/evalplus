```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(input_string):
    if not_palindrome(input_string):
        return input_string
    
    palindrome = input_string[:0:-1] + str(input_string[::-1])
    return palindrome
```
The provided solution uses the two-pointer technique, along with slicing and string concatenation, to construct the shortest palindrome.