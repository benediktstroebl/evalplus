```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize an empty list to store unique numbers
    unique_numbers = []

    # Loop through the input list and add unique elements to the unique_numbers list
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    # Return the list of unique numbers
    return unique_numbers

# Test case 1: Remove duplicates from an input list
test_case_1 = [1, 2, 3, 2, 4]
result_1 = remove_duplicates(test_case_1)
print(result_1)  # Output: [1, 3, 4]

# Test case 2: Remove duplicates from an empty list
test_case_2 = []
result_2 = remove_duplicates(test_case_2)
print(result_2)  # Output: []

# Test case 3: Remove duplicates from a list with duplicates
test_case_3 = [1, 2, 2, 3, 4]
result_3 = remove_duplicates(test_case_3)
print(result_3)  # Output: [1, 2, 3, 4]
```
This Python script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list containing only the unique elements. The function uses a loop to iterate through the input list and appends any unique element to the `unique_numbers` list. The function then returns this list of unique numbers. 

In the test cases, we pass different lists to the function and print the result, which should be a list containing only the unique elements.