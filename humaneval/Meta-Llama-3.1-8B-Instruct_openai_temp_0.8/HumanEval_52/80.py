```python
def below_threshold(lst: list, t: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold t.

    Args:
        lst (list): A list of numbers.
        t (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(num < t for num in lst)


# Example usage
if __name__ == "__main__":
    print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
    print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that takes a list of numbers `lst` and a threshold value `t` as arguments. It returns `True` if all numbers in the list are below the threshold, and `False` otherwise.

The function uses the built-in `all` function in combination with a generator expression to check if all numbers in the list are below the threshold. The `all` function returns `True` if all elements of the iterable are true. If at least one element is false, it returns `False`.

The script also includes example usage of the function at the end.