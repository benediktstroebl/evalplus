```python
def next_smallest(numbers):
    """
    Returns the second smallest element or None if not found.
    """
    if len(numbers) < 2:
        return None
    
    numbers = sorted(numbers)
    return numbers[1] if numbers[0] != numbers[1] else None
```