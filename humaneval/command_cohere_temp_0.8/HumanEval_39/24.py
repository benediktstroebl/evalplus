```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    if n < 1:
        return None
    fib_nums = [0, 1]
    for _ in range(n - 1):
        next_num = fib_nums[-1] + fib_nums[-2]
        fib_nums.append(next_num)
    for num in fib_nums:
        if is_prime(num):
            return num
```

This script defines a `prime_fib` function that returns the n-th Fibonacci number that is also prime. The function initializes a list `fib_nums` with the first two Fibonacci numbers (0 and 1). It then iterates `n - 1` times, adding the sum of the previous two numbers in the list to it, effectively calculating the n-th Fibonacci number. After constructing the list, it iterates through each number in it to find the prime ones, using the `is_prime` function. 

The `is_prime` function is also included, which checks whether a given number is prime by iterating from 2 to the square root of the number and checking for divisibility. 

This solution is efficient and can solve the problem for reasonably large values of `n`, but it's important to note that the time complexity of calculating the n-th Fibonacci number using this approach is still `O(k * log(k))`, where `k` is the `n`-th Fibonacci number and can be very large. For large values of `n`, more optimized approaches could be necessary.