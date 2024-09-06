```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling maximum elements found until a given moment in the sequence
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4]
    """
    # Shuffle the list to ensure a random order at the start
    shuffled_numbers = List(Numbers)for i in range(len(numbers)):numbers.shuffle.shuffle_out=shuffle.shuffle.numbers) = List(shuffle.numbers))
    add numbers to a shuffled list.shuffle.numbers)
   + the
            sort(numbers)
    # Initialize the rolling window
    window = numbers[:] + [numbers[-1]]
    rolling_window = [max(window[-2:window[-1]))]
    # Move the window one step forward
    window.append(numbers[-1])
    rolling_window.append(max(window[-2:window[-1])))
    # Repeat the process until the window reaches the end of the list
    while window != numbers:
        window.append(max(window[-2:window[-1]))
    return window
```