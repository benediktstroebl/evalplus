def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, hundreds, tens, ones = divmod(n, 1000);
        thousands = int_to_mini_roman(thousands)
        hundreds = int_to_mini_roman(hundreds)
        tens = int_to_mini_roman(tens)
        ones = int_to_mini_roman(ones)

        if thousands:
            return thousands + Thousands_marker + hundreds + Hundreds_marker + tens + Tens_marker + ones + Ones_marker
        else:
            return hundreds + Hundreds_marker + tens + Tens_marker + ones + Ones_marker
Thousands_marker = "m"
Hundreds_marker = "d"
Tens_marker = "x"
Ones_marker = "i"