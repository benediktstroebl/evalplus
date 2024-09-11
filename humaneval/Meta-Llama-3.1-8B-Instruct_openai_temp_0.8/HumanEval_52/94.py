Here's a Python script that meets your requirements:
```markdown
# Returns True if all numbers in the list are below the threshold
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Args:
        lst (list): A list of numbers
        threshold (int): The threshold value

    Returns:
        bool: True if all numbers in the list are below the threshold
    """
    return all(num < threshold for num in lst)


# Example usage:
if __name__ == "__main__":
    print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
    print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```
This script uses the built-in Python function `all()`, which returns `True` if all elements in an iterable are true. In this case, we're checking if each number in the list is less than the threshold, which is achieved using a generator expression within `all()`.