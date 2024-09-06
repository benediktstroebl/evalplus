def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, rest = divmod(n, 1000)
        if thousands:
            return "{}m".format(thousands)
        dozens, rest = divmod(rest, 100)
        if dozens:
            return "{}x".format(dozens)
        tens, units = divmod(rest, 10)
        if tens:
            return "{}{}".format(int_to_mini_roman(tens), "i")
        if units:
            return "{}{}".format(int_to_mini_roman(units), "i")
        else:
            return ""