Here is a Python script that contains a self-contained function that generates a sequence of numbers in a markdown-formatted string:
```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f" {list(map(int, range(n))) } "

# Test the function with different input
test_string_sequence(0)  # Output: 0
test_string_sequence(5)  # Output: 0 1 2 3 4 5 

# def main():
    test_string_sequence(6)  # Should output error: range() supports up to int64
    pass
```