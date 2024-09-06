Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block explaining how the solution works:
```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    reverse_mapping = {chr(i + ord("a")): i for i in range(97, 123)}
    return "".join([reverse_mapping.get(ch, ch) for ch in s])
```

The `encode_shift` function shifts every character in a given string `s` by 5 in the alphabet. It does this by taking two steps for each character `ch` in the input string `s`:
1. It converts the character's ASCII value to a number, which is achieved by applying the `ord` function.
2. It calculates the new ASCII value by adding 5 and then taking the remainder when divided by 26 to ensure it stays within the alphabet's range.
3. Finally, it reconstructs the character using the new ASCII value obtained, yielding the encoded string.

The `decode_shift` function reverses the encoding process. It first creates a dictionary called `reverse_mapping`, which maps each encoded character back to its original ASCII value. It then iterates through each character in the input string `s`, and for the encoded characters, it looks up the original ASCII value from the `reverse_mapping` dictionary. Any non-encoded characters are left unchanged. Ultimately, it returns the decoded string. 

This solution allows you to encode and then decode messages using the specified shift mechanism.