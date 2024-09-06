Here's the Python script with a self-contained function that generates and returns a string of space-separated numbers from 0 up to `n`:

```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    numbers = []
    for i in range(n+1):
        numbers.append(i)
    return ' '.join(numbers)

# Example Test Cases
test_string = string_sequence(5)
print("Test String:", test_string)
string_sequence(0)
print("Zero args:", string_sequence())

```
This script defines a function `string_sequence` that takes an integer `n` as an argument and returns a string containing space-separated numbers from 0 to `n`. It uses a simple loop to append numbers from 0 to the `numbers` list and then returns a string using the `join` method.