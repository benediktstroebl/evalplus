Here's a self-contained Python function that implements the rolling max concept you described: 

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling max elements from the given list.
    """
    list comprehension with a rolling window of size 3 and updates the max element accordingly.
    """
    max_element = numbers[0]
    result = [max_element]
    for num in numbers[1:]:
        if num > max_element:
            max_element = num
        result.append(max_element)
    return result
    """

Here, the `rolling_max` function uses a `list comprehension` along with a rolling window of size 3 to keep track of the maximum element. It uses the first element in the list `numbers` as the initial value for `max_element`.

Feel free to test this function using the provided `test_rolling_max` function.