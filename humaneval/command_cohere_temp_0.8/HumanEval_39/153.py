Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    """
    Generates the n-th Fibonacci number that is also prime
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    prev, curr = 0, 1
    for _ in range(n - 2):
        prev, curr = curr, prev + curr
    
    # Start checking from the 6th number (prev + curr + next_candidate)
    # as per fibonacci sequence, next number will always be prev + curr
    candidate = prev + curr
    count = 6
    while not is_prime(candidate):
        candidate = prev + curr
        count += 1
        if count > 1000:  # To prevent infinite loop scenarios
            break
    
    return candidate
```

The script includes a unit test block to verify the correctness of the `prime_fib` function against the provided test cases:
```python
def test_prime_fib():
    # Tests
    assert prime_fib(1) == 2, "1-th prime fibonacci number incorrectly calculated"
    assert prime_fib(2) == 3, "2-th prime fibonacci number incorrectly calculated"
    assert prime_fib(3) == 5, "3-th prime fibonacci number incorrectly calculated"
    assert prime_fib(4) == 13, "4-th prime fibonacci number incorrectly calculated"
    assert prime_fib(5) == 89, "5-th prime fibonacci number incorrectly calculated"

if __name__ == "__main__":
    test_prime_fib()
```

To execute the script, run `python script_name.py` and it should generate the test results accordingly. 

Let me know if it works correctly! I'm happy to provide more explanations or dive deeper into any aspects of the code if needed.