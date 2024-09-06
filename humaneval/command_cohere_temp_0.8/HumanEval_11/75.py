```python
def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(a_char) ^ int(b_char)) for a_char, b_char in zip(a, b))
```

This approach takes advantage of the python 3.7+ type hints and the new `zip` functionality to make the problem solution concise and readable. It uses the `typing` module to specify the input types. The function iterates over the characters of the two strings, and for each pair of corresponding characters, it takes the binary XOR of their ASCII values, converts the result back to a character, and aggregates these characters into a single string. The `zip` function ensures that the corresponding characters are paired and passed to the `chr` function, resulting in the binary XOR of the two strings. This solution is efficient and provides a clear understanding of the process involved in solving the problem.