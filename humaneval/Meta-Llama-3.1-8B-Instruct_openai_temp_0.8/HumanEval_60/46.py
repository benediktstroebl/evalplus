```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    Args:
        n (int): The upper limit of the sum.
    
    Returns:
        int: The sum of numbers from 1 to n.
    """
    return sum(range(1, n + 1))

# Test the function
print(sum_to_n(30))  # 465
print(sum_to_n(100))  # 5050
print(sum_to_n(5))  # 15
print(sum_to_n(10))  # 55
print(sum_to_n(1))  # 1
```

However, the built-in Python function `sum()` is more efficient and Pythonic for this task. 

Alternatively, you could use the arithmetic formula for the sum of an arithmetic series: `n * (n + 1) / 2`.

```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    Args:
        n (int): The upper limit of the sum.
    
    Returns:
        int: The sum of numbers from 1 to n.
    """
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))  # 465
print(sum_to_n(100))  # 5050
print(sum_to_n(5))  # 15
print(sum_to_n(10))  # 55
print(sum_to_n(1))  # 1
```