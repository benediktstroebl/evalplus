def is_multiply_prime(a):
    # check if a is multiples of 2, 3, and 5
    return all(i in [2, 3, 5] for i in a if i == a // 2 == a // 3 == a // 5)