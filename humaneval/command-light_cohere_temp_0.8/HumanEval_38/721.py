Here's the self-contained Python script that includes the `encode_cyclic` and `decode_cyclic` functions, which solve the problem of encoding and decoding a string containing only the characters 'abc':
```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g[1:] + g[0]) if len(g) == 3 else g

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    class in an unusual format.
    """

Here is a sample test:
```python
# sample test
test_encode = "abcdef"
result_encode = encode_cyclic(test_encode)
print("encode:", result_encode)

# test case: valid
test_decode = "cba"
result_decode = decode_cyclic(test_decode)
print("decode:", result_decode)
```

This script defines two functions, `encode_cyclic` and `decode_cyclic`, which solve the problem of encoding and decoding a string containing only the characters 'abc' using a cyclic grouping. The `test_encode` variable is set to a sample string, and the `result_encode` variable is assigned the result of calling the `encode_cyclic` function with the string. Then, the `test_decode` variable is set to another sample string, and the `result_decode` variable is assigned the result of calling the `decode_cyclic` function with the string. Finally, the output is printed for both variables, showing the results of the `encode_cyclic` and `decode_cyclic` functions.