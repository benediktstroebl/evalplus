def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, ones = divmod(n, 1000)
        hundreds, tens = divmod(thousands, 100)
        tens = (tens + 5) // 5
        dozens, singles = divmod(tens, 10)
        result = []
        if thousands:
            result.append(str(thousands) + "m")
        if hundreds:
            result.append(str(hundreds) + "c")
        if dozens:
            result.append(str(dozens) + "x")
        if singles:
            result.append(str(singles) + "i")
        if n == Ones:
            result.append("v")
        return "".join(result)