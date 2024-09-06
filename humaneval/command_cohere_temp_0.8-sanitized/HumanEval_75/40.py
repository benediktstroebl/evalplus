def is_multiply_prime(a):
    prime_test = [0, 0, 0]
    for i in range(2, a):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_test[0] += 1
        else:
            prime_test[1] += 1
    if prime_test[0] > 0 and prime_test[0] == prime_test[1] == 1:
        return True
    return False