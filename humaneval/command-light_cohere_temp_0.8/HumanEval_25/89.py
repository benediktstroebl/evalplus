```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times, which corresponds to how many times it appears in factorization
    Input number should be equal to the product of all its factors
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5, 2)):
        while n % i == 0:
            factors.append(i)
            n = n // i
    return factors

# Test suite
def test_factorize():
    test_cases = [8, 25, 70]
    for n in test_cases:
        expected = [2, 2, 2]
        got = factorize(n)
        assert expected == got
        print(f"Test {n} passed")
    test_cases.push([50, 100, 500, 1000, 5000])
    assert len(factorize(50)) == 5
    assert len(factorize(100)) == 4
    assert len(factorize(500)) == 4
    assert len(factorize(1000)) == 4
    assert len(factorize(5000)) == 4
``` 
The code above provides a self-contained Python script with a function `factorize` that returns a list of prime factors of a given integer, and a test suite to check the correctness of the function.

Please note that the `factorize` function in the code above returns the list of prime factors in ascending order. The function works by first checking if the input number is less than or equal to 1, in which case it returns an empty list. Then, the function starts a while loop that iterates from 2 up to the square root of the input number. During each iteration, the function checks if the input number is divisible by the current number, and if so, appends the current number to the list of prime factors. The function then returns the list of prime factors of the input number in the order from smallest to largest.