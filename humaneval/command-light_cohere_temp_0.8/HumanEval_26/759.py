```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen and num not in numbers[numbers.set() ^ seen]]
    result.copy()
    difference in: [1, 3, 4]

# Test cases
test_data1 = [1, 2, 3, 2, 4, 2, 3, 4]
test_data2 = [1, 2, 3, 4, 5, 4, 6]
test_data3 = [1, 2, 3, 4, 5, 6, 7, 8]

test_results = {
    'test_data1': remove_duplicates(test_data1),
    'test_data2': remove_duplicates(test_data2),
    'test_data3': remove_duplicates(test_data3),
}

print(test_results)
 ``` 
This code defines a function called `remove_duplicates`, which takes a list of integers as input and returns a new list with duplicate values removed. The `seen` set keeps track of numbers that have been seen, and the function iterates through the input list, using the set intersection to determine if a number has been seen before. The output will be a test cases, and the results will be printed to the console.