```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, step(i):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors

def test_factorize(test_num: int) -> None:
    print(test_factorize(test_num))

# Test cases
test_cases = [8, 25, 70]
for test_num in test_cases:
    test_factorize(test_num)
```
The above Python script defines a function called `factorize` that returns a list of prime factors of a given number. It also contains a test cases with different numbers to test the function with. The test cases are passed to the `test_factorize` function, which prints the prime factors of the corresponding test numbers.