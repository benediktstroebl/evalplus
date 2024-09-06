def int_to_mini_roman(num):
    if num < 1000:
        result = []
        for i in range(0, num + 1):
            if i == 0:
                result.append("i")
            elif i == 5:
                result.append("v")
            elif i == 10:
                result.append("x")
            elif i == 25:
                result.append("l")
            elif i == 50:
                result.append("c")
            elif i == 100:
                result.append("d")
            elif i == 250:
                result.append("m")
            elif i == 500:
                result.append("m")
            elif i == 1000:
                result.append("m")
            else:
                result.append(str(i))
        return "".join(result)
    else:
        return "Error! Number must be between 1 and 1000."