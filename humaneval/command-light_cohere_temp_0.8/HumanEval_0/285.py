Here's a self-contained Python function that checks if any two elements in a list are closer than a given threshold:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the list
    numbers.sort()
    
    # Check if the minimum(numbers) <= threshold and any(abs(num1 - num2) for num1, num2 in numbers if num1 != num2) <= 1
                else numbers == []
    return True

# Test the function
numbers = [1.0, 2.0, 3.0, 0.0, 4.0, 5.0, 2.0, 8, 0.0, 0.8]
has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3]
raise ValueError('Test passed invalid data')

The function has_close_elements takes two parameters: a List numbers containing floating-point numbers and a float threshold value. It returns a bool, which is True if any two elements in the numbers list are closer than the threshold value.

The function sorts the numbers list. It then checks if the minimum(numbers) <= threshold. Additionally, it checks if any(abs(num1 - num2) for num1, num2 in numbers if num1 != num2) <= 1. If either condition is met, it returns True. If the conditions are not met, it returns False. 

Finally, it checks if the numbers list is empty and raises a ValueError.