```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_index = numbers.get_max_index()
    max_element = numbers[max_index]
    rolling_max_elements = [max_element]

    for i in range(1, len(numbers)):
        current_element = numbers[i]
        if current_element > max_element:
            max_element = current_element
            max_index = i
        rolling_max_elements.append(current_element)

    return rolling_max_elements

# Example function call and test case
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```
We've defined a function `rolling_max` that generates a list of rolling maximum elements. It uses the maximum element and iterates through the list to find the index of the current maximum element. The script is then tested with a sample input and the output is printed.