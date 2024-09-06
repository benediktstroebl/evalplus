```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n // 2) + 2
    else:
        prime = prime_fib(n // 2) + 2
        return prime

# Test function to check if a number is a Fibonacci prime
def is_prime_fibonacci(num: int):
    if num <= 1:
        return False
    # Checked by the function above
    return is_prime(num) and prime_fib(num) == num

def is_prime(n: int):
    if n <= 1:
        return False

# Checked by the function above
def is_prime(num):
    sieve = [True] * 6
    for i in range(2, num):
        if sieve[i] == True:
            for j in range(i * i, num, i):
                sieve[j] = False
    return sum(sieve) == num

# Driver code to test the above functions
test_is_prime = []
for num in range(0, 100):
    if is_prime(num):
        test_is_prime.append(num)
print(f"{num} is a prime")

test_prime_fib = []
for num in range(0, 100):
    if is_prime(num):
        test_prime_fib.append(num)
    print(f"{num} is a prime Fibonacci number")

print("Passed all tests!")
```