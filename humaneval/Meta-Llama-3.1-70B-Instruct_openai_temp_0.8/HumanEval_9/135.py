```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers representing the rolling maximum.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    rolling_maximums = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        rolling_maximums.append(current_max)

    return rolling_maximums


def main():
    numbers = [1, 2, 3, 2, 3, 4, 2]
    print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]


if __name__ == "__main__":
    main()
```