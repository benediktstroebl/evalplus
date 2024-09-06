```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two elements that are closest to each other.
    """
    first_element = numbers[0]
    second_element = numbers[1]
    
    while first_element > second_element:
        first_element = numbers[0]
        second_element = numbers[1]
    
    return (first_element, second_element)

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)
```