### Cyclic Encoding and Decoding
#### Problem Statement
The problem requires implementing two functions, `encode_cyclic` and `decode_cyclic`, which work with cyclic encoding and decoding of strings.

#### Solution

```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[i:] + group[:i]) if len(group) == 3 else group for i, group in enumerate(groups)]
    
    # Join all groups into a single string.
    encoded_s = ""
    for group in groups:
        encoded_s += group
    
    # Remove extra characters
    encoded_s = encoded_s[:len(s)]
    
    return encoded_s

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # Initialize empty list to store decoded groups.
    decoded_groups = []
    
    # Initialize group as an empty string.
    group = ""
    
    # Iterate over characters in the encoded string.
    for char in s:
        # If group is empty, add character to it.
        if not group:
            group += char
        else:
            # Otherwise, add character to group and append previous group to decoded groups.
            group += char
            decoded_groups.append(group)
            group = ""
    
    # If the last group is not empty, append it to decoded groups.
    if group:
        decoded_groups.append(group)
    
    # Join all groups into a single string.
    decoded_s = ""
    for i, group in enumerate(decoded_groups):
        # If group has fewer elements than 3, shift its elements cyclically.
        if len(group) < 3 and i!= len(decoded_groups) - 1:
            decoded_s += group[-1] + group[:-1]
        else:
            decoded_s += group
    
    # Remove extra characters
    decoded_s = decoded_s[:len(s)]
    
    return decoded_s

# Example usage:
if __name__ == "__main__":
    encoded = encode_cyclic("hello world")
    print("Encoded:", encoded)
    decoded = decode_cyclic(encoded)
    print("Decoded:", decoded)
```

#### Explanation

The provided code implements the `encode_cyclic` and `decode_cyclic` functions as described. 

The `encode_cyclic` function splits the input string into groups of three characters, cyclically shifts each group, and joins them back together to form the encoded string.

The `decode_cyclic` function takes the encoded string, separates it back into groups of three characters, and cyclically shifts each group back to its original position. Finally, it joins all the groups back together to form the decoded string.

In both functions, I've added comments to explain the code and make it easier to understand. Additionally, the example usage at the end demonstrates how to use the functions with the string "hello world".