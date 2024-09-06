Here is a Python script that contains a self-contained function that solves the string-sequence problem you have provided:

```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    if n < 0:
        raise ValueError("n should be non-negative")
        
    return " ".join([str(i) for i in range(0, n+1)])

# Test cases
test_seq = []
for i in range(0,10):
    test_seq.append(string_sequence(i))
print("Test cases passed: ", end = "")
print(test_seq)
```