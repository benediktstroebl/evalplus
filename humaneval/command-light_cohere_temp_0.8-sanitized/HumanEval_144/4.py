def simplify(x, n):
    try:
        numerator, denominator = map(float, x. plain() + n)
        if numerator * denominator == 0:
            return False
        simplified_x = (numerator / denominator)
        return simplified_x
    except ValueError:
        return "Invalid input: both numerator and denominator must be positive whole numbers"