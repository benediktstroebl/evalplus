def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    if n < 61:
        return chr(ord('a') + n - 1)
    else:
        ones, n = divmod(n, 5)
        tens, n = divmod(n, 5)
        hundreds, thousands = divmod(n, 5)
        return min(ones, 3) * 'i' + min(tens, 3) * 'x' + min(hundreds, 3) * 'c' + min(thousands, 3) * 'l'