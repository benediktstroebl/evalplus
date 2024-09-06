Here is a Python script that contains a self-contained function that solves the problem:

```python
from typing import List
from typing import Tuple

def find_closest_elements(numbers: List[float]):
    """ 
    def find_closest_elements(numbers: List[float]):
        # Initialize variables
        min_num = float("inf")
        max_num = 0
        closest_num = None
        closest_other_num = None
        closest_other_num = None
        for num in numbers:
            # Calculate minimum and maximum numbers from list
            min_num = min(min_num, num)
            max_num = max(max_num, num)
            # Determine which is closest and assign it to closest_num
            if num < closest_num:
                closest_num = num
            elif num > closest_num:
                closest_other_num = num
        # Return the two closest numbers in the order of smaller to larger number
        return Tuple[closest_num, closest_other_num]
```

This function takes a list of numbers and returns a tuple of the two closest elements in the list. The function uses theq variables min_num, max_num, closest_num, and closest_other_num. It iterates through numbers in the input list and assigns the minimum and maximum values to the min_num and max_num variables, respectively. It then determines which value is closer and assigns it to closest_num. Then, the closest_num value is assigned to the closest_num variable. Finally, the function returns a tuple of the two closest numbers, with closest_num being the closer number and closest_other_num being the second closest number.