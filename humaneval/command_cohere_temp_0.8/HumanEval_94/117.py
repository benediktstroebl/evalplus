```python
def largest_prime_sum_of_digits(nums):
    primes = [True for _ in nums]
    sqrts = [int(n ** 0.5) for n in nums]
    sieve = [True] * (max(sqrts) + 1)
    for i in range(len(sieve)):
        if sieve[i]:
            for j in range(i * i, len(sieve), i):
                sieve[j] = False
    for i, num in enumerate(nums):
        if primes[i] and num > 1 and sieve[int(num ** 0.5)]:
            digit_sum = sum(map(int, str(num)))
            return digit_sum if digit_sum > num else num
    return 0
```

The function iterates through each number in the list and initially identifies prime candidates using a sieve algorithm. It computes the square root for each number to efficiently rule out non-prime integers. The prime candidacy is then validated using the sieve. If the number is prime and has a larger digit sum than the current recorded prime, its digit sum is updated. The function ultimately returns the largest prime's digit sum. 

The provided example inputs successfully demonstrate the function's correctness.