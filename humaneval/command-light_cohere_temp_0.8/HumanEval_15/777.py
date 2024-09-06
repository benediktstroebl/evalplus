```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n}" * (n + 1)

# Test case 1: Test the function with 0 and 1
print(string_sequence(0)) == '0'
print(string_sequence(1)) == '1'

# Test case 2: Test the function with positive integers
print(string_sequence(5)) == '0 5 10 15 20 25'
print(string_sequence(10)) == '0 10 20 30 40 50'

# Test case 3: Test the function with negative integers
print(string_sequence(-5)) == '0 -5 -10 -15 -20 -25'

# Test case 4: Test the function with large n
print(string_sequence(100)) == '0 100 200 300 400 500 ...'
```
The function uses string formatting with f-string to create the string. It is designed to create the desired sequence of numbers using a simple mathematical formula.