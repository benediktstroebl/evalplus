def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        hundreds, tens, units = divmod(n, 1000)
        return int_to_mini_roman(hundreds) + int_to_mini_roman(tens) + str(units)