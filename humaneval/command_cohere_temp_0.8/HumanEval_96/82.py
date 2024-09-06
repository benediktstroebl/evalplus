Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
# Markdown code block
def count_up_to(n):
    primes = []
    num = 2
    while len(primes) < n:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes
```

This function implements a simple primality testing algorithm to find prime numbers and store them in a list until it reaches a length of `n`. The primality test is a basic optimization of the Euclidean algorithm, where it checks if the number is divisible by any other number in the list of prime numbers found so far. If it is, then that number is not prime, and the for loop breaks early. If not, the number is prime and is added to the list of prime numbers. The function then increments the candidate prime number by 1 and repeats the process until the list of prime numbers has reached a length of `n`. It is worth noting that this method is not the most efficient way to find a list of prime numbers, as it does not optimize for the presence of multiples of primes. However, given the limited scope of the problem, it does produce the required output.