def multiply(a, b):
    result = 0
    while a > 0 or b > 0:
        if a % 10 != b % 10:
            return 0
        else:
            result = result * (a % 10) // (b % 10)
        a = a // 10
        b = b // 10
    return result