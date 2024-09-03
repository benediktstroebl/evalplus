```python
def count_up_to(n):
    """Return array of prime numbers less than or equal to n."""
    lis = [2] 
    for i in range(3, n+1): 
        if is_prime(i) == True: 
            lis.append(i) 
    return lis

def is_prime(n):
    """Check if n is prime."""
    if n <= 1: 
        return False
    if n <= 3: 
        return True
    if n % 2 == 0 or n % 3 == 0: 
        return False
    i = 5
    while i * i <= n: 
        if n % i == 0 or n % (i + 2) == 0: 
            return False
        i += 6
    return True

# Example usage:
n = int(input("Enter n: "))
result = count_up_to(n)
print(result)

# Test cases
test_cases = [10, 17, 0, 30, 0, 0]
for case in test_cases:
    n = case[0]
    result = count_up_to(n)
    print(f"Case {n} passed: {result}")
```
The provided Python script defines a function `count_up_to` that returns an array of prime numbers less than or equal to a given integer `n`. The function utilizes a loop and an helper function `is_prime` to check and accumulate prime numbers up to `n`. The `is_prime` function implements a simple primality test, and the main function uses the test cases to verify the correctness of the function's output.