def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, rest = divmod(n, 1000)
        if thousands:
            return f"mm{int_to_mini_roman(thousands)}io"
        else:
            hundreds, tens = divmod(rest, 100)
            if hundreds:
                return f"cx{int_to_mini_roman(hundreds)}{int_to_mini_roman(tens)}{int_to_mini_roman(n // tens % 10)}"
            else:
                return f"x{int_to_mini_roman(tens)}{int_to_mini_roman(n // tens % 10)}"