```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # iterate over list
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # check if two numbers are less than given threshold
            if numbers[i] - numbers[j] < threshold:
                return True
    return False

# test case
test_data = [1.0, 2.0, 3.0, 0.0, 5.0]
test = has_close_elements(test_data, 0.0)
print(test_test)

``` 
The function checks the elements of the list and returns a boolean value indicating whether any two numbers are closer to each other than the given threshold. 

This function can be used to determine if any two numbers in a list are close to each other or not.