```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    """
    necessary cases:
        1. All prime factors are
        a number is 1, return []
        2. The number is divisible by 2, return [2]
        3. All factors are not numbers of  2n+1 ( n is a factor), return list of [2, n] for all n
        4. All factors are not numbers of form 4k+1 with k>1, return [2, 4k] for all k
        """
    # 1. All factors are same numbers of 2n+1
    # 2. All factors are numbers of form 4k+1 with k>1
    # 3. All factors are numbers of form 4k+1 with k>1
    # 4. All factors which n is not divisible by 2, 3, or 5, return list of [n]
    # 5. All factors are which are divisible by 7, return [7]
    # 6. All factors which n is is a perfect square, return []
    # 7. All factors which n is is 1 or 2, return [1]
    # 8. All factors which n is is 3, return [3]
    # 9. All factors which n is not a factor of 5, return []
    # 10. All factors which n is is a factor of 7, return [7]
    if n <= 2:
        return []
    elif n % 2 == 0:
        return [2]
    elif n % 3 == 0:
        return [2, 3]
    elif n % 5 == 0:
        return [5]
    elif n % 7 == 0:
        return [7]
    elif n % 9 == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    elif n % 4 == 0:
        return [2, 2]
    elif n == 3:
        return [3]
    elif n % 6 == 0:
        return []
    else:
        return [n]
```
This script defines a function factorize, which takes an integer n as input and returns a list of prime factors of the input number in order from smallest to largest. The factors are listed number of times corresponding to how many times each factor appears in the factorization of the number.