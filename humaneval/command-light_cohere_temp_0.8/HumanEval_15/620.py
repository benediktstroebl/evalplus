Here's the code:
```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)
    ```
This code defines a function called string_sequence that takes an integer n as input and returns a string containing space-delimited numbers starting from 0 up to n inclusive. The function uses the string formatting with f-string and the repeat operator * (n + 1) to achieve the desired result.