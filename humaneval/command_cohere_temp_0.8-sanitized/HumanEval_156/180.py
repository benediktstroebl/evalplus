def int_to_mini_roman(num):
    if num == 1:
        return "i"
    elif num == 4:
        return "iv"
    elif num == 5:
        return "v"
    elif num == 9:
        return "ix"
    elif num == 10:
        return "x"
    elif num == 40:
        return "xl"
    elif num == 50:
        return "l"
    elif num == 90:
        return "xc"
    elif num == 100:
        return "c"
    elif num == 400:
        return "cd"
    elif num == 500:
        return "d"
    elif num == 900:
        return "cm"
    elif num == 1000:
        return "m"
    else:
        return ""