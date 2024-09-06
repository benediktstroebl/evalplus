```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n //= i
    for num in factors:
        while n % num == 0:
            factors.remove(num)
    return factors
``` 
This Python code defines a function factorize that calculates and returns a list of prime factors of a given integer n. The function follows a algorithm of factoring by trial and removal, where it iteratively tries divisors until the number becomes prime, adding them to the list of factors. It handles the cases of even even numbers as input, and the time complexity of the algorithm is O(log n), making it efficient for larger numbers.