def is_simple_power(x, n): 
    if n == 1 or x == n:
        return True
    elif n % 2 == 0:
        return (x**(n // 2)) == x
    else:
        return x**n == x