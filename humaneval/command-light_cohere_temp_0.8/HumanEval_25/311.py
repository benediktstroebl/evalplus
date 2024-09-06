```python
def factorize(n):
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
        
    for i in range(3, int(n**0.5) + 1, step by step):
        while n % i == 0:
            factors.append(i)
            n = n // i
        
    return factors

# Test cases
test_factorize = []
test_factorize.push([25, 8, 25, 70])
test_factorize.pop()()
test_factorize.push([3, 16])

# Test function execution
for x in test_factorize:
    actual_factors = factorize(x)
    assert actual_factors == [2, 2, 2]  # case 1
    assert actual_factors == [5, 5]  # case 2
    assert actual_factors == [2, 5, 7]  # case 3
```

This Python code defines a function called `factorize` that aims to find and return the list of prime factors for a given integer `n`. The function uses a loop to continuously divide by numbers from 2 up to the square root of `n`, checking for divisibility. The prime factors are then added to the `factors` list. The code also includes a test suite with a few test cases to ensure the correctness of the `factorize` function.