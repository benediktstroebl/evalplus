def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, ones = divmod(n, 1000)
        hundreds, tens = divmod(thousands * 10, 100)
        tens += ones * 10
        dozens, singles = divmod(tens, 10)
        result = []
        if dozens:
            result.append(dozens * "x")
        if hundreds:
            result.append(str(hundreds) + "l")
        if tens:
            result.append(str(tens) + "x")
        if singles:
            result.append(str(singles) + "i")
        return "".join(result)