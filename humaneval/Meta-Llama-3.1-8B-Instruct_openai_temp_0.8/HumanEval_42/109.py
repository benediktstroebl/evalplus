### Increment List Elements

Here is a self-contained Python script that defines a function `incr_list` to increment each element in a given list by 1:

```markdown
### Code
```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): List of numbers to increment.

    Returns:
        list: List with elements incremented by 1.
    """
    return [x + 1 for x in l]

# Example usage:
if __name__ == "__main__":
    print(incr_list([1, 2, 3]))
    print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

### Explanation

This script defines a function `incr_list` that uses a list comprehension to create a new list where each element is the original element plus 1.

The `if __name__ == "__main__":` block provides example usage of the `incr_list` function. When the script is run directly (not imported as a module), this block is executed and prints the results of incrementing the example lists.