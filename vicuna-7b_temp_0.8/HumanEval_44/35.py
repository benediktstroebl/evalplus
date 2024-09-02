

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    # Let's use a list of all possible cases where base is less than 10
    cases = [["", "0"]]
    for i in range(1, 10):
        cases.append([f"{i:02X}", f"{i:02b}")]

    # We'll use a dictionary to store the number of digits in the base
    num_digits = {}
    for i in range(1, 10):
        num_digits[i] = x // i

    # We'll use a dictionary to store the representation of the number in each base
    base_reps = {}
    for i in range(1, 10):
        base_reps[i] = [None]

    for x in range(1, 10):
        for base in cases[x % 10]:
            if x % base == 0:
                digits_found = 0
                while x % base == 0:
                    digits_found += 1
                    x //= base
                digits_found = digits_found // 2 + 1
                if digits_found > num_digits[base]:
                    raise ValueError(f"Invalid base {base}")
                base_reps[base][len(base_reps[base]) - 1] = str(x)
                break

    return base_reps[base][len(base_reps[base]) - 1]
