```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
``` 

The function takes in a list of numbers `numbers` and an int `delimiter` as inputs. It iterates through the list, excluding the `delimiter` from the result list, and adds the `delimiter` to the result list the number of times required to match the length of the original list. This approach ensures that the `delimiter` is inserted between every two consecutive elements of the `numbers` list, as described in the problem statement.