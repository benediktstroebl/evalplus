### Solution
```markdown
### below_threshold.py
```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold, False otherwise.

    Args:
        numbers (list): A list of numbers to check.
        threshold (int): The threshold value.

    Returns:
        bool: Whether all numbers are below the threshold.
    """
    return all(num < threshold for num in numbers)

# Example use cases:
if __name__ == "__main__":
    print(below_threshold([1, 2, 4, 10], 100))  # Expected: True
    print(below_threshold([1, 20, 4, 10], 5))   # Expected: False
```

### Explanation
The `below_threshold` function uses the built-in `all` function with a generator expression to check if all numbers in the list are below the threshold. If the list is empty, `all` will return `True` because there are no numbers to check.