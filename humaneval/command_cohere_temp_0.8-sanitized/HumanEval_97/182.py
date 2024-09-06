def multiply(a, b):
    num_a = str(a)
    num_b = str(b)
    p = 0
    for i in range(max(len(num_a), len(num_b))):
        if len(num_a) <= i:
            digit_a = 9
        else:
            digit_a = int(num_a[i])
        if len(num_b) <= i:
            digit_b = 9
        else:
            digit_b = int(num_b[i])
        p = (p + digit_a * digit_b) % 10
    return p