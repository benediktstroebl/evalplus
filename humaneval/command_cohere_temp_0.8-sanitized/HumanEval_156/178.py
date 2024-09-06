def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        hundreds, remainder = divmod(n, 5)
        if hundreds == 0:
            return str(remainder) + "i"
        tens, ones = divmod(remainder, 5)
        if tens == 0:
            return ["", "v", "ix", "l", "iv"][hundreds] + (ones + 1) * "i"
        else:
            return ["", "v", "ix", "l", "iv"][hundreds] + str(tens) + (ones + 1) * "i"