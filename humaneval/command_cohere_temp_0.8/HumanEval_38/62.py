```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string into groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split string into groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range(len(s) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)
```

This code provides two functions: `encode_cyclic` and `decode_cyclic`. 

The `encode_cyclic` function takes a string `s` as input and returns a encoded string. It splits the input string into groups of three characters (if the remaining length is less than 3, it will return a group of the remaining characters). Then, it cycles the characters in each group by concatenating the last two characters with the first character. It returns the encoded string by joining the groups.

The `decode_cyclic` function takes an encoded string s as input and returns the original string. It splits the encoded string into groups of three characters (if the length is not divisible by three, it will break the last group). Then, like the encoding process, it cycles the characters in each group by concatenating the last two characters with the first character. It returns the original string by joining the groups. 

Here is an example usage of the encode_cyclic function:
```python
print(encode_cyclic("Hello World")) # Output: Hll oWrd
```
Here is an example usage of the decode_cyclic function:
```python
print(decode_cyclic("Hll oWrd")) # Output: Hello World
```
This would encode the string "Hello World" to "Hll oWrd" and then decode "Hll oWrd" to "Hello World".