def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        tens = int(n) // 10
        if tens == 1:
            return "x" + int_to_mini_roman(n % 10)
        elif tens <= 3:
            return str(tens) + "x" + int_to_mini_roman(n % 10)
        else:
            return str(tens) + int_to_mini_roman(n % 10)