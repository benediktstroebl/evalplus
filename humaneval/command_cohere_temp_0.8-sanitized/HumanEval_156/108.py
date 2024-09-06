def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, ones = divmod(n, 1000)
        hundreds, tens = divmod(thousands, 100)
        tens = (tens + 5) // 5
        tens = ("i" * tens) + "x" * (tens == 0)
        hundreds = "c" * hundreds + tens_to_mini_roman(ones)
        return hundreds + "m" * (thousands > 0)
def tens_to_mini_roman(n):
    if n == 1:
        return "i"
    elif n == 2:
        return "ii"
    elif n == 3:
        return "iii"
    elif n == 4:
        return "iv"
    elif n == 5:
        return "v"
    else:
        return "x" * (n - 5)