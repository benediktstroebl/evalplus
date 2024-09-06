def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        hundreds, remainder = divmod(n, 5)
        if hundreds == 0:
            return str(remainder) + "i"
        tens, ones = divmod(remainder, 5)
        if tens == 0 and ones == 0:
            return "xv"
        if tens == 0:
            return str(ones) + "i"
        if ones == 0:
            return str(tens) + "x"
        return str(tens) + str(ones) + "i"