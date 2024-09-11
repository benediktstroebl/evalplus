### Solution

Here's a Python script that includes a function to check if all numbers in a list are below a given threshold.
```python
def below_threshold(l: list, t: int) -> bool:
    """
    Return True if all numbers in the list l are below threshold t.

    Args:
        l (list): A list of numbers.
        t (int): The threshold.

    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(i < t for i in l)

# Example usage
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```
This script uses the built-in `all()` function in combination with a generator expression to check if all numbers in the list `l` are below the threshold `t`. The `all()` function returns `True` if all elements of the iterable (in this case, the generator expression) are true. If at least one element is false, `all()` returns `False`.