def int_to_mini_roman(n):
    if n < 1000:
        result = []
        for x in range(0, n + 1):
            if x != 0:
                result.append(mini_roman[x])
        result.reverse()
        return ''.join(result)
    else:
        return 'Error!'
mini_roman = ['i', 'iv', 'ix', 'lx', 'lc', 'ld', 'lm']