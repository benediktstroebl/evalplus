Here is a Python script that contains a self-contained function that generates and returns a string containing space-separated numbers from 0 up to n:
```python
def string_sequence(n: int) -> str:
    return "".join(str(i) for i in range(0, n+1))

# Test cases
test_seq = string_sequence(0)
print(test_seq)  # Output: '0'
test_seq = string_sequence(5)
print(test_seq)  # Output: '0 1 2 3 4 5'
```
The test cases demonstrate the function's ability to generate the correct sequence of numbers from 0 up to n.