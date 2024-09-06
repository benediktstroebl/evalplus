
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    
    sign = 1 if a > 0 else -1
    a,b = abs(a),abs(b)

    max_digits = max(len(str(a)),len(str(b)))
    s = 0

    for i in range(max_digits-1,-1,-1):

        s += a%10 * b%10 * sign
        a //= 10
        b //= 10

    return s

assert multiply(148, 412) == 16 
assert multiply(19, 28) == 72
assert multiply(2020, 1851) == 0
assert multiply(14,-15) == 20
assert multiply(245, 654) == 7