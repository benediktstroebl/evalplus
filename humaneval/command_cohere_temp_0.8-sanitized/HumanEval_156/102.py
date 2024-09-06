def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, rest = divmod(n, 1000)
        if thousands:
            return f"m{int_to_mini_roman(thousands)}m{int_to_mini_roman(rest)}"
        else:
            hundreds, rest = divmod(n, 100)
            if hundreds:
                return f"c{int_to_mini_roman(hundreds)}{int_to_mini_roman(rest)}"
            else:
                tens, ones = divmod(n, 10)
                if tens:
                    return f"x{int_to_mini_roman(tens)}{int_to_mini_roman(ones)}"
                else:
                    return f"{int_to_mini_roman(ones)}"