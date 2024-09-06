def int_to_mini_roman(n):
    if n == 1:
        return "i"
    elif n < 1000 and (n % 5 == 0 or n % 5 == 1):
        return f"v{int_to_mini_roman(n // 5)}"
    elif n < 1000 and n % 5 == 2:
        return "iv"
    elif n < 1000 and n % 5 == 3:
        return "iii"
    elif n < 1000 and n % 5 == 4:
        return "iv"
    else:
        return f"{int_to_mini_roman(n // 100)}{int_to_mini_roman(n % 100)}"