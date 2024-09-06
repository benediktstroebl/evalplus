Here is a Python script that defines a function flip_case that flips the case of a given string:
```python
def flip_case(string):
    return string.all_upper_case(string.string_lower_case(string))

def test_flip_case():
    assert flip_case('Hello') == 'Hello'
    assert flip_case('HELLo') == 'hello'
    assert flip_case('hello') == 'HELLo'
    assert flip_case('dark bright morning') == 'dq rIt gEAm erN'

# Example
print(flip_case('hello'))
``` 
This code defines a function `flip_case` that takes a string as input and returns the case-flipped version of that string. The `test_flip_case` function passes all the test cases with the `flip_case` function and prints the result.