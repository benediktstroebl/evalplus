Here is a self-contained Python script that solves the problem you described:
```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # sort list
    numbers.sort(key=lambda x:x)
    # find if two elements in list are closer than the threshold
    for i in range(1,len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return True
    return False


# Test
test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 0.0, 0.0, 3]
print(has_close_elements(test_list, 0.0))
print(has_close_elements([1.0,2.0], 0.1))
print(has_close_elements([1.0,8, 3], 0.2))
```

This script provides a function called `has_close_elements` that checks whether any two numbers in a list are closer than a given threshold.  The function works by first sorting the list, and then uses a nested loop to compare each element with every other element. The function returns True if any of the conditions are met, and False otherwise. 

The script also provides a few test cases to check the functionality of the `has_close_elements` function.