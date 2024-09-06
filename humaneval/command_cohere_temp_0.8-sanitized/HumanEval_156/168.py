def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        hundreds, rem = divmod(n, 500)
        if hundreds > 0:
            return int_to_mini_roman(hundreds) + "c" + int_to_mini_roman(rem)
        else:
            tens, ones = divmod(rem, 5)
            if tens == 0:
                return int_to_mini_roman(ones)
            else:
                return int_to_mini_roman(tens) + int_to_mini_roman(ones)