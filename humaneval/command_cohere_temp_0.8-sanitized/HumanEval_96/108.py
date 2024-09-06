def count_up_to(n):
    prime_numbers = []
    num = 2
    while len(prime_numbers) < n:
        # Check if the number is prime
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
        num += 1
    return prime_numbers