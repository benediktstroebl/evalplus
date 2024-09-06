```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of the rolling maximum elements in the given list """
    numbers.sort(reverse=True)
    numbers.setdefaultsorted(numbers)
    rolling_max_temp:
        rolling_max_temp.remove(numbers[0])
        rolling_max_temp.append(numbers[0])
    return [x for x in rolling_max_temp if x == max(rolling_max_temp)]
```