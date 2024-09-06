```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n):
        if n % i == 0:
            j = n // i  #candidate
            if j > i:  # candidate is larger than divisor
                return j
            elif i == j:  # divisors are the same
                return i
    return 1  # if no candidates are found, return 1
```

This algorithm leverages Python's built-in exhaustion checking via ranges and ternary operations, which efficiently find the largest divisors and their corresponding divisors. It is streamlined to provide an optimal solution in a single loop, without introducing complex logic.