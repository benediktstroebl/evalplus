def is_multiply_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    # Multiply Prime
    if n < 100:
        count = 0
        for i in range(2, int(n ** (1/2)) + 1):
            if is_prime(i) and is_prime(n // i):
                count += 1
        return count == 2
    else:
        return False