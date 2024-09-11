Here's a Python function that meets the given requirements:
```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.

    Examples:
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
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))   # 465
print(sum_to_n(100))  # 5050
print(sum_to_n(5))    # 15
print(sum_to_n(10))   # 55
print(sum_to_n(1))    # 1
```
However a simpler way of implementing this is by using a loop (which isn't needed in this case because we can calculate the sum directly with a simple formula).
However if you wanted to do it with a loop you could do:
```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.

    Examples:
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
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum

# Test the function
print(sum_to_n(30))   # 465
print(sum_to_n(100))  # 5050
print(sum_to_n(5))    # 15
print(sum_to_n(10))   # 55
print(sum_to_n(1))    # 1
```
This loop is not the most effective way to solve this problem but it is an example of how you could use a loop to solve it.