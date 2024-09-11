### Increment List Elements

Here's a self-contained Python script that defines a function `incr_list` to increment all elements in a list by 1:
```markdown
### incr_list.py

```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): Input list of elements.

    Returns:
        list: List with elements incremented by 1.

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]


# Example usage:
if __name__ == "__main__":
    print(incr_list([1, 2, 3]))
    print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
### Run the script:

To run the script, save it as `incr_list.py` and execute it using Python:
```bash
$ python incr_list.py
```
This will output the incremented lists as expected.

### Notes:

* The `incr_list` function uses a list comprehension to increment each element in the input list by 1.
* The function takes a list as input and returns a new list with the incremented elements.
* The function includes docstrings for documentation and readability.
* The example usage demonstrates how to call the function and print the results.