Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block demonstrating the implementation:
```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    reverse_mapping = {chr(i): chr((i - ord("a") + 26) % 26 + ord("a")) for i in range(97, 123)}
    return "".join(reverse_mapping.get(ch, ch) for ch in s)
```

The functions `encode_shift` and `decode_shift` are implemented in this script to encode and decode a string respectively, using a simple substitution cipher. Here's an example usage of these functions:
```python
def test_encode_shift():
    assert encode_shift("hello") == "ifmmp"
    assert encode_shift("world") == "zdnd"

def test_decode_shift():
    assert decode_shift("ifmmp") == "hello"
    assert decode_shift("zdnd") == "world"

test_encode_shift()
test_decode_shift()
```

The above functions test the `encode_shift` and `decode_shift` functions against a couple of simple inputs. When executing the entire script, these test functions will be run automatically.  Any doubts regarding the implementation or usage can be clarified in the comments.  This implementation is just a basic example, as there are better techniques for doing encryption and decryption efficiently.  This approach is simple and direct, making it suitable for beginner programmers to understand.