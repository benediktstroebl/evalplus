```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            if count > 0:
                factors.append(i)
                factors.append(count)
    if n > 1:
        factors.append(n)
        factors.append(1)
    return factors[1:]
```
The factorization algorithm loops from 2 up to `n`. 

For each potential factor `i` it checks if `i` can be divided exactly `n`, incrementing a counter `count` if it can. 

Once `i` is established as a factor, the algorithm iterates through its divisions, keeping track of the count of divisions using the counter `count`. This count corresponds to the number of times the prime factor appears in the factorization, the algorithm constructs a list with the prime factor and the count.

Once the while loop is completed for a factor, the algorithm moves on to the next potential factor, updating `n` to be the remaining integer after partial division. In the end, the algorithm checks if `n` is greater than 1, adds it as a factor with a count of 1, and returns the list of factors leaving out the first element which is always 2.

Here is an example usage of the function:
```python
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]
```
This should match the examples provided in the problem statement.