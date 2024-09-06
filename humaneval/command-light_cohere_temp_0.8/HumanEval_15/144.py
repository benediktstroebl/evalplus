Here is a Python script that defines a function string_sequence that returns a string containing space-delimited numbers starting from 0 up to the number n:

```python
def string_sequence(n: int) -> str:
    return "".join(str(i) for i in range(0, n+1))
```

This is a self-contained function that uses the built-in range function to generate the sequence of numbers from 0 to n, and the str function to convert each number into a string. The function is tested by passing the test case of string_sequence(0), which should return the string '0'.