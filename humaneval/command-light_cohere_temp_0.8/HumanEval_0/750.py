```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    Return: boolean value 
    """
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return True
    return False

# Example usage
input_list = [1.0, 2.0, 3.0, 0.0, 4.0]
print (has_close_elements(input_list, 0.0)) 
```