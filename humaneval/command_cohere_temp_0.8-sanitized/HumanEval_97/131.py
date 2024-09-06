def multiply(a, b):
    num_a = a % 10
    num_b = b % 10
    product = num_a * num_b
    if product > 9:
        return 0
    else:
        return product