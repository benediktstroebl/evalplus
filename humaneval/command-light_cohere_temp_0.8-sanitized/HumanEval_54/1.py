def same_chars(s0: str, s1: str):
    return all(c0 == c1 for c0, c1 in zip(s0, s1))