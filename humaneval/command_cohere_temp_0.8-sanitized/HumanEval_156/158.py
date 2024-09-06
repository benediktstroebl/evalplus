def int_to_mini_roman(n):
    if n < 1:
        return ""

    # Exception handling for edge cases
    if n == 1:
        return "i"
    if n == 10:
        return "x"
    if n == 100:
        return "c"

    # Convert decimal to binary