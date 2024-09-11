```markdown
### Unique Elements in a List
#### Python Script

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

# Example usage
if __name__ == "__main__":
    print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

### Explanation
1. We define a function `unique` that takes a list `lst` as input.
2. Inside the function, we convert the list to a set using `set(lst)`. This automatically removes any duplicate elements.
3. We then convert the set back to a list and sort it in ascending order using `sorted`.
4. Finally, we return the sorted list of unique elements.
5. In the example usage, we call the `unique` function with a sample list and print the result.
```