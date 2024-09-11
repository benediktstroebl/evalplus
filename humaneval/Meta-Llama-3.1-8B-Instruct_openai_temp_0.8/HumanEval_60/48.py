```python
# sum_to_n.py

def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    
    total = n
    for i in range(1, n):
        total += i
    
    return total

# Example usage
if __name__ == "__main__":
    print(sum_to_n(30))  # Output: 465
    print(sum_to_n(100))  # Output: 5050
    print(sum_to_n(5))  # Output: 15
    print(sum_to_n(10))  # Output: 55
    print(sum_to_n(1))  # Output: 1
```

However, the previous solution can be optimized for large values of `n` by using the formula for the sum of an arithmetic series: `n * (n + 1) / 2`.

```python
# optimized_sum_to_n.py

def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    
    return n * (n + 1) // 2

# Example usage
if __name__ == "__main__":
    print(sum_to_n(30))  # Output: 465
    print(sum_to_n(100))  # Output: 5050
    print(sum_to_n(5))  # Output: 15
    print(sum_to_n(10))  # Output: 55
    print(sum_to_n(1))  # Output: 1
```

This optimized solution is more efficient, especially for large values of `n`, as it avoids the need for a loop.