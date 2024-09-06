Here's a self-contained Python function that returns a string containing space-delimited numbers starting from 0 up to the number n:
```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return ' '.join([str(i) for i in range(n)])

# Test cases
test_str = string_sequence(0)
print("Test Case 1:", test_str)

test_str = string_sequence(5)
print("Test Case 2:", test_str)

test_str = string_sequence(-5)
print("Test Case 3:", test_str)

test_str = string_sequence(10)
print("Test Case 4:", test_str)
```
The above code defines a function `string_sequence` that returns a string containing space-separated integers from 0 up to n. It then provides some test cases which are passed to the function and printed out to the console.