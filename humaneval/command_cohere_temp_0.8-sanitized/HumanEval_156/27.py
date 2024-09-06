def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        tens, remainder = divmod(n, 5)
        if remainder == 0:
            return f"({tens}x{tens})"
        elif remainder == 1:
            return f"({tens}x{tens}-{int_to_mini_roman(1)})"
        else:
            return f"({tens}x{tens}-{int_to_mini_roman(remainder)})"