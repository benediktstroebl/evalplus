Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """Check if an integer is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    primes = []
    for i in range(2, n+1):
        if is_prime(i) and i < n:
            primes.append(i)
            count += 1
            if count == n:
                break
    return primes
```
The provided code contains two functions. The `is_prime` function checks if a given integer is a prime number by iterating from 2 up to the square root of the number and checking for divisibility. The `count_up_to` function takes an integer `n` as input and initializes an empty list `primes` to store the prime numbers found within the range from 2 to `n`. It then iterates through the range, checking if each number is prime using the `is_prime` function. If a prime number is found and it is also less than `n`, it is added to the `primes` list. The loop continues until the count of prime numbers reaches `n` or exceeds `n`, respectively. The function returns the `primes` list, which contains the first `n` prime numbers less than `n`.

Here is an example of how you can use the above code to solve the problem:
```python
count = count_up_to(20)
print(count)
```
This would print out `count_up_to(20) => [2,3,5,7,11,13,17,19]`. 

The code efficiently solves the problem by first checking for primality using the `is_prime` function and then iterating through the remaining numbers to collect the required prime numbers.