```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    >>> has_close_elements([1.0, 2.0, 3.0], 0.6)
    }Yes this8 
    # Check if the elements in the list are numbers
    >>> if all(num for num in numbers if isinstance(num, (int, float)))):
        # Check if any two numbers are closer than the threshold
        for i in range(len(numbers)//2):
            for j in range(i+1, len(numbers)):
                if abs(numbers[i]-numbers[j]) <= threshold:
                    return True
        return False
    return True
```
This code defines a function called `has_close_elements` that takes in a list of numbers and a threshold as input and returns a boolean value indicating if any two numbers in the list are closer than the threshold. 

The function first checks if all the elements in the list are numbers, and if so, it checks if any two numbers are closer than the threshold. It then iterates over thees over half of the list and compares each pair of elements to check if they are closer than the threshold. 

Finally, the function returns True if it found any pair of elements that satisfied the condition and returns False otherwise.