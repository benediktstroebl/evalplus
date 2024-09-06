def int_to_mini_roman(n):
    if n == 1:
        return "i"
    elif n < 5:
        return str(n) + "i"
    elif n < 10:
        return str(n) + "v"
    elif n < 50:
        return str(n)[:1] + str(n)[1:] + "i"
    elif n < 100:
        return str(n) + "l"
    elif n < 200:
        return str(n)[:1] + str(n)[1:] + "l"
    elif n < 500:
        return str(n) + "x"
    elif n < 700:
        return str(n)[:1] + str(n)[1:] + "x"
    elif n < 1000:
        return str(n)[:1] + str(n)[1:] + "m"