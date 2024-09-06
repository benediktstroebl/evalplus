def starts_one_ends(n):
    pos_ints = [str(i) for i in range(1, n + 1)]
    # Append invariants: n-digit integer that starts with 1 and n-digit integer that ends with 1
    pos_ints.extend('1' + x for x in pos_ints)
    pos_ints.extend(x + '1' for x in pos_ints)
    # Remove duplicates
    pos_ints = list(set(pos_ints))
    return len(pos_ints)