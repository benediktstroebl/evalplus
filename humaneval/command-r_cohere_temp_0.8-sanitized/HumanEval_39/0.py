def prime_fib(n: int):
    """
    Finds the n-th Fibonacci number that is also a prime.
    """
    fib_seq = [2, 3]
    while len(fib_seq) < n + 1:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        # Only keep numbers that are prime
        if is_prime(fib_seq[-1]):
            fib_seq.pop()

    return fib_seq[n]
def is_prime(num: int) -> bool:
    """Check if num is a prime number."""
    if num == 2:
        return True
    if num <= 1 or num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True