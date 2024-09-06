

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
    # all groups are length 3
    groups = list(s)
    # restore groups
    groups = [(groups[i] + groups[i + 1] + groups[i + 2]) for i in range(0, len(groups), 3)]
    # restore original order
    groups = "".join(groups)
    # replace for readability
    groups = groups.replace("0", "a")
    groups = groups.replace("1", "b")
    groups = groups.replace("2", "c")
    groups = groups.replace("3", "d")
    groups = groups.replace("4", "e")
    groups = groups.replace("5", "f")
    groups = groups.replace("6", "g")
    groups = groups.replace("7", "h")
    groups = groups.replace("8", "i")
    groups = groups.replace("9", "j")
    groups = groups.replace("a", "0")
    groups = groups.replace("b", "1")
    groups = groups.replace("c", "2")
    groups = groups.replace("d", "3")
    groups = groups.replace("e", "4")
    groups = groups.replace("f", "5")
    groups = groups.replace("g", "6")
    groups = groups.replace("h", "7")
    groups = groups.replace("i", "8")
    groups = groups.replace("j", "9")
    groups = groups.replace(" ", "")
    return groups

