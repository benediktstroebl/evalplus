```python
def sort_third(lst):
    """Sorts a list such that numbers divisible by three are in their correct positions,
    and numbers not divisible by three maintain their original order.
    Input:
    list lst
    Returns: sorted list lst such that all numbers divisible by three are in their
    original positions, and all other numbers remain in their original order."""
    return sorted(lst, key=lambda x: x // 3)
```