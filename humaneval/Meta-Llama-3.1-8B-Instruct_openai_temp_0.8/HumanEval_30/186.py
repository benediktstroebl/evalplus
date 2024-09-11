```markdown
### Problem: Filter Positive Numbers in a List

The following Python script utilizes a list comprehension to filter a list of numbers and return only the positive integers.

#### Code

```python
def get_positive(numbers: list):
    """
    Return a list of only positive numbers from the input list.
    
    Args:
    numbers (list): A list of integers.
    
    Returns:
    list: A list of positive integers.
    
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]
```

#### Example Usage

```python
print(get_positive([-1, 2, -4, 5, 6]))  # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123, 1]
```
```
#### Explanation

The `get_positive` function uses a list comprehension to filter the input list `numbers`. It iterates over each number `num` in the list and includes it in the output list if it's greater than zero (`num > 0`). This approach is concise and efficient for filtering positive numbers from a list.