def unique_digits(xs):
    # Check if the list is empty or not
    if not xs:
        return []

    # Sort the list in increasing order and remove duplicates
    ys = list(set(xs))
    zs = []
    for y in ys:
        # If the number has any even digit, skip
        if any(d % 2 == 0 for d in str(y)):
            continue
        # If the number only has odd digits, add to the list
        zs.append(y)

    return zs