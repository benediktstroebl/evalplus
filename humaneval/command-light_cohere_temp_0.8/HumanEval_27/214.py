```python
def flip_case(string):
    return ''.join_to_uppercase(string)[::-1]

# Test cases
assert flip_case('Hello') == 'olleH'
assert flip_case('olleH') == 'hello'
```  This script defines a function flip_case, which takes a string as input and returns a new string with the characters' cases flipped. The test cases ensure that the expected output for the input strings 'Hello' and 'olleH' are correctly returned by the function.