def int_to_mini_roman(n):
    if n < 1000:
        result = []
        for x in range(n, 0, -1):
            if x == 5:
                result.append('v')
            elif x == 10:
                result.append('x')
            elif x == 25:
                result.append('xx')
            elif x == 50:
                result.append('l')
            elif x == 100:
                result.append('c')
            elif x == 250:
                result.append('cc')
            elif x == 500:
                result.append('d')
            elif x == 1000:
                result.append('m')
            else:
                result.append(str(x))
        return ''.join(result)
    else:
        return ''