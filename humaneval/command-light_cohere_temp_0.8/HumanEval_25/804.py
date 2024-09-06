```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times which corresponds to how many times it appears in factorization of the number.
    """ Example note that all numbers below a given number would be even, so would be removed from the list.
    # Example number is always greater than 2, so all even numbers will be removed. 
    if n <=2, return []
    if n < 2: return []
    # remove even numbers
    even_numbers = [x for x in range(2, n+1) if x%2 == 0]
    even_numbers.extend(iter(map(lambda x: x, even_numbers)))
    # remove all multiples of 2
    multiple_of_2 = [x for x in range(2, n+1) if x%2 * x%2 == 0]
    multiple_of_2.extend(iter(map(lambda x: x, multiple_of_2)))
    # remove all numbers that are divisible by n
    divisible_by_n = [x for x in range(n+1) if x% n == 0]
    divisible_by_n.extend(iter(map(lambda x: x, divisible_by_n)))
    # return list of prime factors
    factors = [x for x in range(2, n+1) if x not in even_numbers and x not in multiple_of_2 and x not in divisible_by_n]
    return factors
``` 
This script defines a function called **factorize** that takes an integer n as input and returns a list of its prime factors. The function starts by checking if n is less than 2, and if so, it returns an empty list. Then, it removes even numbers from the list, as they are even and greater than 2. The function also removes all multiples of 2 and all numbers that are divisible by n. Finally, it returns a list of prime factors of the original number n.