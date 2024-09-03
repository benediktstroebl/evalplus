def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Input values are not provided.")
    if a == 0 or b == 0:
        return 0

    c = a
    while b > 0:
        if b % a == 0:
            b, c = b // a, c // a
        else:
            break
    return c