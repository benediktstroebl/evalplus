```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Steps:
    1. Identify the unique factorss
    prime factors
    2.
    3.
    n must be factored by a smallest prime divisor.
    until the unique primes are identified
    """

    return [d for d in range(2, int(n**0.5) + 1) if n % d == 0 for d in range(2, int(n**0.5))]

test_factorize = []
test_factorize.push(25, [2, 5])
test_factorize.push(50, [2, 25])
test_factorize.push(70, [2, 5, 7])
test_factorize.push(100, [2, 2, 5, 25])

def main():
    print(factorize(100))

main()
```

The script provides a function `factorize` which returns the list of prime factors of a given number `n` in the order of decreasing magnitude. The function uses the straightforward algorithm to factorize the number and returns a list of prime factors. The function is then tested with a series of numbers using another function `test_factorize` and the results are printed.