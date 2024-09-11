```markdown
## Unique Elements in a List

This script defines a function `unique` that takes a list as input, removes duplicates, and returns the sorted unique elements.

### Code

```python
def unique(lst: list) -> list:
    """
    Return sorted unique elements in a list.

    Args:
        lst (list): The input list.

    Returns:
        list: A sorted list of unique elements.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

### Explanation

The function uses a combination of the `set` and `sorted` functions to achieve the desired result. Here's a step-by-step breakdown:

1. `set(lst)`: This converts the input list to a set, which automatically removes duplicates. Sets in Python are unordered collections of unique elements.
2. `sorted(...)`: This function sorts the elements in the set in ascending order.

By combining these two functions, we get a single function `unique` that takes a list as input, removes duplicates, and returns the sorted unique elements.

Note that this implementation has a time complexity of O(n), where n is the length of the input list, making it efficient for large inputs. However, it does not preserve the original order of elements. If you need to preserve the original order, you can use a different approach, such as using a dictionary or a collections.OrderedDict.