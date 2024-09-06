```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses a list comprehension to iterate through each character in the input string. For alpha characters, it uses the `swapcase()` method to flip between uppercase and lowercase. Non-alpha characters are unchanged and included as-is in the output. 

To test this script, you can run the following input tests to ensure the function correctly flips the case for various characters:
```python
assert flip_case('Hello') == 'hELLO'
assert flip_case('xyZaPy') == 'xyZaPy'
assert flip_case('123') == '123'
assert flip_case('all CAPS') == 'ALL iPS'
```