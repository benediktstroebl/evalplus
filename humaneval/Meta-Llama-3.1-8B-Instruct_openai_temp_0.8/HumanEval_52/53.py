Here's a Python script that includes the `below_threshold` function:
```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.
    
    Returns:
        bool: True if all numbers are below threshold, False otherwise.
    """
    return all(num < threshold for num in lst)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 4, 10], 100),
        ([1, 20, 4, 10], 5),
    ]

    for test_case in test_cases:
        lst, threshold = test_case
        result = below_threshold(lst, threshold)
        print(f"Test Case: {lst}, Threshold: {threshold}, Result: {result}")
```
In this script, we define the `below_threshold` function using type hints for clarity. The function uses the built-in `all()` function in combination with a generator expression to check if all numbers in the list are below the threshold. The `all()` function returns `True` if all elements in the iterable (in this case, the generator expression) are `True`, and `False` otherwise.

We then include some test cases in the `if __name__ == "__main__":` block to demonstrate the function's usage. The `test_cases` list contains tuples of input lists and threshold values, which are passed to the `below_threshold` function and the results are printed.