def is_multiply_prime(a):
    # Write a function that returns true if the given number is the multiplication of 3 prime numbers
    # and false otherwise
    limit = int(sqrt(a)) + 1
    for b in range(3, limit, 2):
        if a % b == 0:
            continue
        for c in range(3, limit, 2):
            if a % c == 0:
                continue
            if b == c:
                return False
            for d in range(3, limit, 2):
                if a % d == 0:
                    return False
                if b == d or c == d:
                    return False
    return True