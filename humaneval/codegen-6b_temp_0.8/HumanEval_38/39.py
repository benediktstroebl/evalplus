

def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    def convert(c1, c2, c3):
        output = chr(ord(c1) + 1) + chr(ord(c2) + 1) + chr(ord(c3) + 1)
        if output[0] == "z":
            output = "a" + output[1:]
        return output

    i = 0
    decoded_str = ""

    while i < len(s):
        # three consecutive characters
        c1 = s[i]
        c2 = s[i + 1]
        c3 = s[i + 2]
        s1 = ord(c1)
        s2 = ord(c2)
        s3 = ord(c3)
        output = convert(c1, c2, c3)
        decoded_str += output
        i += 3

    return decoded_str


cyclic_test_strings = ["123", "7a8b", "bab", "zazbz"]
cyclic_test_results = ["123", "7a8b", "bab", "zyzba"]

for test_string, result in zip(cyclic_test_strings, cyclic_test_results):
    print("Cyclic: {0}".format(test_string))
    print("\tCyclic Encoded: {0}".format(encode_cyclic(test_string)))
    print("\tCyclic Decoded: {0}".format(decode_cyclic(encode_cyclic(test_string))))
    print("\tExpected: {0}".format(result))
    print("\n")

