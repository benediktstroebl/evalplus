def int_to_mini_roman(number):
    if number <= 1000:
        return f"{number:d}".lower()
    else:
        return int_to_mini_roman(number - 1000) + 'x'