def is_multiply_prime(a):
    prime_test = [0, 0, 0]
    for i in range(2, a):
        if a % i == 0:
            prime_test[0] = 1
        if i * i > a:
            break
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            prime_test[1] = 1
        if i * i > a:
            break
    if a > 4:
        for i in range(3, int(a**0.5) + 1, 2):
            if a % i == 0:
                prime_test[2] = 1
            if i * i > a:
                break
    return all(prime_test)