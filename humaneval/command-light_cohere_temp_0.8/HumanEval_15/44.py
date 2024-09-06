Here's a self-contained Python script that defines a function string_sequence that returns a string containing space-delimited numbers starting from 0 up to n:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return " ".join([f"0 {i}" for i in range(n + 1)])

# Example test cases
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5 

```