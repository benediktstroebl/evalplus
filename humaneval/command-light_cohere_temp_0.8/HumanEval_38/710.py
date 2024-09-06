```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of three characters
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   

    test 1:
        echo ' aa112233aa ' >> decode_cyclic
    test 2:
        echo '   aa112233aa   ' >> decode_cyclic
    test 3:
        echo 'aa112233aa' >> decode_cyclic
    test 4:
        echo '\n   aa112233aa   \n' >> decode_cyclic
    test 5:
        echo 'aa112233aaa' >> decode_cyclic
    test 6:
        echo 'aa112233aa'aa' >> decode_cyclic
    test 7:
        echo 'aa112233aa'  ' >> decode_cyclic
    test 8:
        echo '\n    aa112233aa  \n' >> decode_cyclic
    test 9:
        echo ' aa123456aa ' >> decode_cyclic
    test 10:
        echo 'aa112233' >> decode_cyclic

This code defines two functions, `encode_cyclic` and `decode_cyclic`, to solve the problem of encoding and decoding a string of characters based on a cycle of three characters. The encode_cyclic function splits the string into groups of three characters, cycles the characters in each group, and then joins the elements back together to form the original string. The `decode_cyclic` function takes an input string encoded with the `encode_cyclic` function and returns the decoded string. 

You can add more test cases to this script to test the functionality of the `encode_cyclic` and `decode_cyclic` functions.