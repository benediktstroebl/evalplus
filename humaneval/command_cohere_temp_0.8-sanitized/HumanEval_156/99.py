def int_to_mini_roman(n):
    if n < 1:
        return ""

    res = []
    for curr_char, max_val in enumerate(string.ascii_lowercase):
        for i in range(1, 13):
            if n >= i:
                res.append(curr_char)
                n -= i
                if n == 0:
                    break
            elif n > 0:
                res.append(str(n))