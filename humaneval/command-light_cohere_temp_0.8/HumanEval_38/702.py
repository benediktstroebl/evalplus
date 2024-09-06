```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    fact encoded string
   
    is of the form <enc group_ >
    where each group is a string of length 3.
    return decoded string
    if s[0] != '<'
    # decode the string
    return s[1:].decode() if s[0] == '>'
    # handle invalid input
    return "Invalid input"

# Example usage
string = "hello world"
print(encode_cyclic(string))  # expected output: <<-"hwww lllol dlro"
print(decode_cyclic(string))  # expected output: "hello world")
``` 
The code defines two functions: encode_cyclic and decode_cyclic. The encode_cyclic function takes a string as input and returns an encoded string by cycling groups of three characters. The decode_cyclic function takes an input string and returns the decoded string. The code also provides an usage example to test the functions with the string "hello world".