def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    if n < 61:
        return ['i', 'iv', 'v', 'ix', 'xl', 'l', 'xc', 'c', 'cd', 'd', 'cm', 'm'][n]
    else:
        hundreds = int_to_mini_roman(n // 100)
        tens = int_to_mini_roman(n % 100)
        return f'{hundreds}{tens}'