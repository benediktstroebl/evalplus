def int_to_mini_roman(n):
    if n == 1:
        return "i"
    elif n == 4:
        return "iv"
    elif n == 5:
        return "v"
    elif n == 9:
        return "ix"
    elif n == 10:
        return "x"
    elif n == 40:
        return "xl"
    elif n == 50:
        return "l"
    elif n == 90:
        return "xc"
    elif n == 100:
        return "c"
    elif n == 400:
        return "cd"
    elif n == 500:
        return "d"
    elif n == 900:
        return "cm"
    elif n == 1000:
        return "m"
    else:
        result = []
        for i in range(1000):
            if n >= i:
                result.append(int_to_mini_roman_recursive(i))
                n -= i
        result.reverse()
        joined_result = ""
        for roman in result:
            joined_result += roman
        return joined_result
def int_to_mini_roman_recursive(n):
    if n == 1:
        return "i"
    elif n == 4:
        return "iv"
    elif n == 5:
        return "v"
    elif n == 9:
        return "ix"
    elif n == 10:
        return "x"
    elif n == 40:
        return "xl"
    elif n == 50:
        return "l"
    elif n == 90:
        return "xc"
    elif n == 100:
        return "c"
    elif n == 400:
        return "cd"
    elif n == 500:
        return "d"
    elif n == 900:
        return "cm"
    elif n == 1000:
        return "m"
    else:
        result = int_to_mini_roman_recursive(n//10)
        if n%10 > 0:
            result += int_to_mini_roman_recursive(n%10)
        return result