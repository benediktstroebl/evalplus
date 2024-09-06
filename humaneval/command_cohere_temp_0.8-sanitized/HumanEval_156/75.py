def int_to_mini_roman(n):
    if n == 1:
        return "i"
    elif n < 5:
        return str(n) + "i"
    elif n < 10:
        return str(n) + "ii"
    elif n < 50:
        return str(n) + "iii"
    elif n < 100:
        return str(n) + "iv"
    elif n < 500:
        return str(n) + "v"
    elif n < 1000:
        return str(n)[:-1] + str(n)[-1] + "ix"