```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Selecting two closest elements
    closest1 = float('inf')
    closest2 = float('-inf')
    for num in numbers:
        if num > closest1:
            closest1 = num
        elif num > closest2:
            closest2 = num
    else:
        return closest1, closest2
    
    return closest1, closest2
``` 
Do you have any other questions about Python scripting or other topics that I can help you with?