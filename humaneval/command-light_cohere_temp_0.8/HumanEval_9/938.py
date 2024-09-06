```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling maximum elements found in the given list of integers
    """
    max_element = numbers[0]
    result = [max_element]
    for num in numbers[1:]:
        current = num
        max_element = max(max_element, current)
        result.append(max_element)
    return result

def test_rolling_max(numbers):
    return [rolling_max(numbers)[0] == numbers[0]]

# Example usage
test_data = [1, 2, 3, 4, 5]
test_result = test_rolling_max(test_data)
print(test_result)  # Output: [True]
``` 
This Python script presents a method rolling_max designed to generate a list of rolling maximum elements within a given sequence of integers. It employs a `max_element` to begin the sequence and progressively updates this maximum element while appending the most current value to the result list.

The script also includes a function test_rolling_max which assesses whether the rolling_max function appropriately produces the initial element of the input list. 

Finally, an example usage demonstrates the functionality of the rolling_max function by applying it to a test list and confirming that the initial element is correctly detected.