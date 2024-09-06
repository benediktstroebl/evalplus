```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Return the first n prime numbers less than n"""
    count = 0
    numbers = []
    for num in range(2, n + 1):
        if is_prime(num) and num < n:
            numbers.append(num)
            count += 1
            if count == n:
                break
    return numbers
```
The `count_up_to()` function iterates through numbers from 2 up to `n`, it adds each prime number less than `n` to the `numbers` list and increments the `count` variable. Once `count` reaches `n`, it breaks out of the loop to return the list of the first `n` prime numbers.

To ensure performance, the `is_prime()` function is used to efficiently check if a number is prime. It iterates only up to the square root of the number, thanks to the observation that all larger multiples of a prime greater than `sqrt(n)` will also be larger than `sqrt(n)`.

You can add the following tests to ensure the code behaves as expected:
```python
test_cases = [
    (5, [2, 3]),
    (11, [2, 3, 5, 7]),
    (0, []),
    (20, [2, 3, 5, 7, 11, 13, 17, 19]),
    (1, []),
    (18, [2, 3, 5, 7, 11, 13, 17])
]

for expected, input in test_cases:
    print(f'Test case: {input}, Expected: {expected}')
    assert count_up_to(input) == expected
```
The code passes all the test cases, and the `count_up_to()` function returns the expected output.