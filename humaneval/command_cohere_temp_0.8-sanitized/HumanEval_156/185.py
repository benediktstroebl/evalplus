def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        hundreds, roman = "", ""
        while n > 0:
            notch = n % 10
            roman = str(notch) + roman
            n //= 10
            if n == 0:
                hundreds = roman
                break
        return hundreds + roman