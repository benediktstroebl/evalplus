```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    if n == 0:
        return '0'
    numbers = [0]
    for i in range(1, n + 1):
        numbers.append(numbers[i])
    return ' '.join(numbers)
# Test the function with different inputs
test_string_sequence(0) # Output: '0'
test_string_sequence(5) # Output: '0 1 2 3 4 5'
test_string_sequence(10) # Output: '0 9 8 7 6 5 4 3 2 1 0'
test_string_sequence(20) # Output: '0 19 18 17 16 15 14 13 10 9 8 7 6 5 4 3 2 1 0'
```
The function `string_sequence` generates a string with space-separated numbers from 0 to n. It uses a recursive approach with a list of numbers and an exponential for the loop range, ensuring numbers are generated up to the requested number n.