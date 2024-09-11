```python
def incr_list(l: list):
    """
    Return list with elements incremented by 1.

    Args:
        l (list): Input list with numbers.

    Returns:
        list: List with elements incremented by 1.

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]
```

You can run this script in your Python environment to test the `incr_list` function. Here's how you can do it:

```python
import doctest

def main():
    doctest.testmod()

if __name__ == "__main__":
    main()
```

This script uses the `doctest` module to automatically test the `incr_list` function based on the examples provided in the docstring. If all tests pass, the script will run without any errors.