Here is a self-contained Python script that defines a function that solves the problem of generating a sequence of numbers in a markdown code block:
```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3} {n+4}"

# Test cases
test_sequence = [
    "test_seq_01",
    n=10,
    expected="0 10 11 12 13 14 15 16 17 18 19 20"
]
test_sequence()

# Usage
text = string_sequence(5)
print(text)
```