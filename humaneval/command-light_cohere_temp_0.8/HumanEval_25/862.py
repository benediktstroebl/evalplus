```python
def factorize(n: int) -> List[int]:
    factors = []
    for i in range(1, int(n**0.5)+1):
        while n % i == 0:
        factors.append(i)
        n //= i
    factors.append(n)
    return factors
```
This script defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function works by iterating through the numbers from 1 to the square root of `n` (plus one), and checking each number for divisibility. If a number divides `n`, it is appended to the list of factors. The function then returns the list of prime factors of `n`, in order from smallest to largest.

To test the function, you can run the script and call the `factorize` function with different values of `n`. This will return the list of prime factors for that value of `n`.