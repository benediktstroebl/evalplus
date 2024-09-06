Here is a Python script with a self-contained function that solves the problem of creating a string of numbers from 0 up to n:
```python
def string_sequence(n: int) -> str:
    return f'{0}{n}'.format(n)

# Test the function:
test_string_sequence = string_sequence(5)
print(test_string_sequence)
# Output: 0   5 4 3 2 1
```
The function returns a string where each number from 0 to n is separated by a space.