```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    s = s.split(' ',')
    ungrouped sequence of substrings of length 3. groups with every three substrings
    if group has fewer elements than three, will return empty string.
    groups = [map(lambda x:x[:3], s))
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    decodes the prepared s using
    string.
    groups = s.split(' ',')
    map(lambda x:x.groups = decode_cyclic(x) for x in groups), return "".join(groups))

# Example test cases
test_str = "abc,def,ij,kl,xy,z,w,u,v,x,b,a,c"
test_str = "abc,abc,def,ijk,ijkl,xy,z,w,u,v,x,b,c"
test_str = "abc,def,,ijkl,xy,z,w,u,v,x,b,a,c"
test_str = "abcdef,ijkl,xyztu,bc"

print(encode_cyclic(test_str))  # Output: abcd,def,ijkl,xy,z,w,u,v,x,b,a,c
print(decode_cyclic(test_str))  # Output: abcdefijklxyztucbc
```

The function encode_cyclic takes a string s as input and returns an encoded version of s, which is a string where the characters at each group of three consecutive characters are joined together with a period separator. The function is designed to handle any input string that contains at least three consecutive characters. The function split the process the code, which is a recursive process. The function encode_cyclic splits s into a list of substrings of length three, and then uses a map to cycle through the substrings. The map returns a mapping each subset to its corresponding cycle of three consecutive characters. The function then joins the elements of each cycle with a period separator and returns the result.

The function decode_cyclic takes an encoded string s as input and returns a decoded version of s, which is a string where the characters are split into groups of three consecutive characters. The function is designed to handle any input string that is encoded using the encode_cyclic function. The function uses a split process code, which is a recursive process. The function decode_cyclic splits s into a list of substrings of length three, and then uses a map to cycle through the substrings and join them back together with a period separator. The function then returns the groups.