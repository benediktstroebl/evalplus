def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / max(len(s0), len(s1)) > 0.6