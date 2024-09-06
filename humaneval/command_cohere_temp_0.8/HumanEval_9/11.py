Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_max_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the
    given moment in the sequence. Returns empty list if rolling_max_window is empty."""
    return list(map(max, window(numbers, rolling_max_window)))

def window(numbers: List[int], window_size: int) -> Iterator[Tuple[int, ...]]:
    """Generator function returning sliding window of given size over the list of numbers."""
    for i in range(len(numbers)-window_size+1):
        yield numbers[i:i+window_size]
```

The `rolling_max()` function takes two arguments: `numbers`, which is the list of integers, and `rolling_max_window`, which specifies the rolling window size. It uses the `window()` function to create an iterator over sliding windows of the specified size. It then maps the max function over each window to find the maximum element in each window.

The `window()` function is a generator function that produces sliding windows of the specified size over the list of numbers. It takes a list of integers and an integer window_size as arguments and yields tuples of integers representing the windows.

This code uses type hints and docstrings to improve readability and maintainability. It also avoids mutating the original list by using the map function and an iterator, which can improve performance for large lists. 

This solution is general and can be adapted to more complex scenarios.