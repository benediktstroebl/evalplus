def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x < 0:
            y = -x
            z = x + y
        else:
            # Find the second largest positive integer that hasn't been seen yet
            y = max([z for z in l[i + 1:] if z > x and z not in seen])
            # Assume the third one is the negative of the largest positive integer
            # that hasn't been seen yet
            z = -l[-1] if l[-1] > y and l[-1] not in seen else -y
        if y and z and x != 0 and y + z == 0 and x not in seen and y not in seen and z not in seen:
            return True
        seen.add(x)
    return False