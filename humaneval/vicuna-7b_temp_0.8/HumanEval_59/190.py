

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 3:
        return n
    if n % 2 == 0:
        return None
    for num in range(3, int(n ** 0.5) + 1, 2):
        if n % num == 0:
            return num
    return n

n = int(input("Enter an integer: "))
if n < 3:
    print("Number must be at least 3.")
    exit()
if n % 2 == 0:
    print("Number is even.")
    exit()
prime_factors = []
for i in range(3, int(n ** 0.5) + 1, 2):
    if n % i == 0:
        prime_factors.append(i)
        break
else:
    prime_factors.append(n)
for i in prime_factors:
    if i > largest_prime_factor(n):
        largest_prime_factor(n) = i
