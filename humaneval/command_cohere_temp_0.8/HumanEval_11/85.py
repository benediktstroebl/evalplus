```python
def string_xor(a, b):
    return a.translate(str.maketrans('01','10')) == b.translate(str.maketrans('10','01'))
```

This approach uses the `translate` function with custom translations to achieve XOR logic between two binary strings. 

To further clarify the logic behind this solution:
- '01' is used for translating bitwise XOR '1' to '0' and '0' to '1'.
- '10' is used for translating bitwise XOR '0' to '1' and '1' to '0'.

By using the translate method with these translations on each input string, the result is a string that represents the binary XOR of the original inputs.