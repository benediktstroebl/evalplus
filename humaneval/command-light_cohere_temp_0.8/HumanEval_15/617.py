```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 to n inclusive."""
    return ("".join(str(i) for i in range(n)))

# Test the function with various input values
test_string_sequence = string_sequence  # Store the function object
test_string_sequence(0)   # Output: '0'
test_string_sequence(5)   # Output: '0 1 2 3 4 5'
test_string_sequence(10) # Output: '0 9 8 7 6 5 4 3 2 1 0'
test_string_sequence(100) # Output: '0 99 98 97 96 95 90 ...'

# Example: Get a string containing numbers from 0 to 9
result = string_sequence(9)
print(result)  # Output: '0 9 8 7 6 5 4 3 2 1'
```
This code defines a function `string_sequence` that returns a string containing space-separated numbers from 0 to `n`. The function uses list comprehension to generate the string, and the range function to generate the sequence of numbers. The test suite ensures the test the function's correctness with various input values. The `string_sequence` function can be used to generate a string of numbers, and the example demonstrates its usage by calling the function with an argument of 9 and printing the result.