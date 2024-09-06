

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
    if not s:
        return ""
    # we want to [(1, 2, 3), (4, 5, 6), (7, 8, 9), ...]
    # length of permutations is 3^n where n is the length of the string.
    permutations = list(itertools.permutations(range(3), len(s) // 3))
    # for each permutation, find matching cylic substrings.
    for permutation in permutations:
        match = True
        for i in range(len(s) // 3):
            match = match and s[i * 3 + permutation[i]] == s[(i + 1) * 3 + permutation[i]]
            match = match and s[i * 3 + permutation[i]] == s[(i + 2) * 3 + permutation[i]]
        if match:
            # get each part of the permutation that must be cycled.
            groups = [s[i * 3:(i + 1) * 3] for i in range(len(permutation))]
            # return the permuted string truncated to the original length.
            return "".join(groups) + s[len(groups) * 3:]
    return ""

