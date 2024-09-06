def unique_digits(xs):
    # Check if the list is empty or not
    if not xs:
        return []

    # Sort the list in increasing order and remove duplicates
    ys = list(set(xs))
    zs = []
    for y in ys:
        if not any(c % 1 == 0 for c in str(y)):
            zs.append(y)
    return zs