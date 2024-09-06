```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n //= 2
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                n //= i
            else:
                i += 1
        factors.append(n)
    return factors
```

This function, `factorize()`, calculates the list of prime factors of a given integer `n` by trial and error. The function uses a approach of trying to divide by 2 first, and then checking for divisibility by squares of integers up to the square root of `i`.  The function returns the list of prime factors in ascending order. 

Let's break down the code:
- Importing the `List` typing: This line imports the `List` typing from the `typing` module.
- Defining the function `factorize`: This function takes an integer `n` as input and returns a list of its prime factors. It uses a method `while n > 1` to repeatedly check if `n` is divisible by 2, adding 2 to the list of factors if it is divisible by 2, and dividing `n` by 2 to move on to the next step.
- The loop starts by checking if `n` is divisible by 2. If it is, it adds 2 to the list of factors and divides `n` by 2 to move to the next step.
- If loop starts again, checking if `n` is divisible by the square of `i`. If it is, it adds `i` to the list of factors and divides `n` by `i` to move to the next step.
- The function returns the list of prime factors in ascending order.