def multiply(a, b):
    num_a = str(a)
    num_b = str(b)
    p = 0
    for i in range(max(len(num_a), len(num_b))):
        p *= int(num_a[i] or '9') * int(num_b[i] or '9')
        p //= 10
    return p