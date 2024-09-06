```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two closest numbers in the list and returns them in order (smaller number, larger number).
    """
    if len(numbers) < 2:
        return numbers[0]
    else:
        left, right = numbers[0], numbers[1]
        for num in numbers[2:]:
            distance = (num - left)**2 + (right - num)**2
            if distance < 0:
                left, right = num, num
            elif distance == 0:
                continue
            else:
                break
        return left, right
```

This function takes a list of numbers as input and returns a tuple of the two closest numbers in the list, in order of them being the smaller number and the larger number. It uses the first nested loop to find the two closest numbers. The function first checks if the list has at least two elements and if it does, it returns the first element as the smaller number. If the list has less than two elements, it assumes that the first element is the smaller number and the second element is the larger number, so it returns the first element as the smaller number. The function then uses the maximum likelihood algorithm to find the two closest elements.