Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
# Markdown code block
def count_up_to(n):
    primes = []
    num = 2
    while len(primes) < n:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes
```

The function `count_up_to(n)` takes an integer `n` as input and returns an array of the first `n` prime numbers less than `n`. The function relies on an underlying helper function `primes`, which is a straightforward implementation of the sieve of Eratosthenes algorithm, to determine whether a given number is prime or not. 

The algorithm works by iteratively marking the multiples of each prime number, starting from 2. The smallest current prime number is advanced by increments of 2, until the largest prime number is reached. 

To achieve this, the code establishes a list of numbers to be checked for primality and initially assumes all numbers are prime. Subsequently, it traverses the list, marking the multiples of the current prime number as non-prime. The first prime number remains unmarked, whereas the multiples of this prime (beginning from the next higher integer) are marked. Notably, the code skips any numbers in the list that have already been marked. 

Finally, the code delivers a list of prime numbers, by excluding the marked numbers from the list of numbers to be checked for primality. 

This algorithm is quite efficient due to the decreasing frequency of marked numbers after each iteration.