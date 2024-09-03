```python
def count_up_to(n):
    result = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i**0.25) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            result.append(i)
    return result

# Test cases for the function
test_cases = [
    0,
    1,
    2,
    5,
    10,
    18,
    20,
    # Add more test cases as needed
]

for case in test_cases:
    print(count_up_to(case))
``` 
This code defines a function `count_up_to` that generates a list of prime numbers up to a given non-negative integer `n`. It uses a nested loop to iterate from 2 to `n`, checking each number for primality using a simple primality test. The function then returns a array of prime numbers less than or equal to `n`.  This approach efficiently generates the desired list of primes.  The use this function with various input values to test its behavior and correctness.