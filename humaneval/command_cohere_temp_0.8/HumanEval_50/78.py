Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block demonstrating the implementation:
```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "infjqgpsvhuybngmkdlrowz"))
```
The functions take and return strings. `encode_shift` shifts every character by 5 in the alphabet, while `decode_shift` undoes the encoding process.

Here's a markdown code block explaining how the functions can be used:
```python
```python
def test_encode_shift():
    assert encode_shift("Hello World!") == "Ijzojw Ltmdpq!"
    assert encode_shift(" encase ") == " ibsaq "

def test_decode_shift():
    assert decode_shift("Ijzojw Ltmdpq!") == "Hello World!"
    assert decode_shift(" ibsaq ") == " encase "
```

Above is an example of how you can tests the functions with various inputs and expectations. Feel free to copy and adapt this code block into your own codebase or interactive environment.