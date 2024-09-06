```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   okenize encoding involves converting all characters except spaces to
    lowercase and removing spaces.
    return "".join(s.tokenize encoding).
    return s

if __name__ == "__main__":
    s = input("Input string: ")
    print(s, "Decoded:", encode_cyclic(s), "Encoded:", decode_cyclic(encode_cyclic(s)))
```
This script defines a function named `encode_cyclic` that takes an input string and returns an encoded string. The function uses the string slicing and mapping to divide the input string into groups of three characters, and then cycles through the characters in each group. The `decode_cyclic` function is defined to take an input string and return a decoded string. The function tokenizes the encoding by converting all characters except spaces to lowercase and removing spaces. 

The script also includes a `main` function that takes user input, prints the input string, performs decoding and encoding using the `encode_cyclic` and `decode_cyclic` functions, respectively, and then prints the results.