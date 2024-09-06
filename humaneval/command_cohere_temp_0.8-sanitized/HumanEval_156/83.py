def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        tens = int(str(n)[-1])
        if tens == 0:
            return int_to_mini_roman(n-1) + "i"
        elif tens == 5:
            return int_to_mini_roman(n-5) + "v"
        else:
            return int_to_mini_roman(tens) + int_to_mini_roman(n-tens-1)