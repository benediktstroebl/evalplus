def unique_digits(xs):
    # Check if the list is empty or not
    if not xs:
        return []

    odd_digits = [int(''.join(x for x in str(n) if x.isdigit()) or 99999) for n in xs]
    return sorted(odd_digits)