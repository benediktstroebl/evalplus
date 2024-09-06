def unique_digits(xs):
    # Check if the list is empty or not
    if not xs:
        return []

    odd_digits = [int(''.join(x for x in str(n) if x.isdigit())) for n in xs if not any(int(x) % 2 == 0 for x in str(n))]
    return sorted(odd_digits)