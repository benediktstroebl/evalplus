### Filtering Positive Numbers in a List
#### Python Script

```markdown
### Positive Numbers Filter

This script filters out non-positive numbers from a given list.

#### Code
```python
def get_positive(numbers: list) -> list:
    """
    Return only positive numbers in the list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: A list of positive numbers.

    Examples:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]

### Example Usage
if __name__ == "__main__":
    numbers = [-1, 2, -4, 5, 6]
    positive_numbers = get_positive(numbers)
    print("Positive numbers:", positive_numbers)
```

#### Explanation

This script defines a function `get_positive` that takes a list of numbers as input. It uses a list comprehension to filter out non-positive numbers by checking if each number is greater than 0. The resulting list of positive numbers is returned.

The script also includes an example usage section, where we create a list of numbers, call the `get_positive` function, and print the result.

#### Running the Script

Save this code in a file (e.g., `positive_numbers.py`) and run it using `python positive_numbers.py`. You should see the output:
```
Positive numbers: [2, 5, 6]
```