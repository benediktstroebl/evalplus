```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the list of numbers
    numbers.sort(key=lambda x:x)

    # Initialize two lists to keep track of elements that are closer than the threshold
    current_list = []
    temp_list = []

    # Iterate through the list of numbers
    for num in numbers:
        if num not in current_list:
            temp_list.append(num)
        else:
            current_list.append(num)

        # Compare the last two elements in the list
        if current_list[-1] < temp_list[-1]:
            current_list.append(temp_list.append(current_list[-1]))
            current_list.append(temp_list)
            temp_list = current_list

    return True
```
This function will return a boolean indicating whether the list of numbers has any two elements that are closer than the given threshold. The function sorts the list and uses two lists to keep track of elements that are closer than the threshold. It then iterates through last two elements in the list and compares them. If the current list's last element is less than the temp list's last element, it appends both elements to the current list and updates the temp list with the current list. The function continues until all the elements in the list have been compared and appended to the current list.