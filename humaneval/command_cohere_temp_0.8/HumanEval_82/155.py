```python
def is_prime_length(input_str):
    if len(input_str) == 1:
        return True
    elif len(input_str) <= 3:
        return False
    else:
        divisible = 2
        while divisible * divisible <= len(input_str):
            if len(input_str) % divisible == 0:
                return False
            divisible += 1
    return True
```

The condition for checking if the string length is equal to 1 has been moved to the beginning of the function to ensure immediate clarity on this aspect. The function will return True since strings of length 1 are by definition prime.

Furthermore, the function now reduces the loop increment step by step, which helps optimize the runtime. It calculates the square root of the length and uses that value as an upper limit for the `divisible` variable, iterating through potential divisors up to that number. This reduction in iterations results in a more efficient algorithm.