Here's a self-contained Python function that performs the XOR operation on two input strings: 

```python
def string_xor(a: str, b: str) -> str:
    """
    Xor two strings a and b
    Returns: string
    """
    if not a:
        a = '0'
    if not b:
        b = '0'

    result = '0'
    for c in a + b:
        if c == '0':
            continue
        result ^= c

    return result
``` 

This function performs the XOR operation on the strings, handling edge cases like empty input strings gracefully. 

You can use this function by passing two strings as arguments, and it will return the XOR of those strings.