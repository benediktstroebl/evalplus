```markdown
### Solution to the Problem

#### Problem Statement
Given a list of numbers and a threshold, return True if all numbers in the list are below the threshold.

#### Code
```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.

    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(num < threshold for num in lst)


# Example usage
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))  # Output: False
```

#### Explanation
The `below_threshold` function uses the built-in `all` function in combination with a generator expression to check if all numbers in the list are below the threshold. The `all` function returns True if all elements in the given iterable (in this case, the generator expression) are true. If any element is false (i.e., a number is above the threshold), `all` returns False.