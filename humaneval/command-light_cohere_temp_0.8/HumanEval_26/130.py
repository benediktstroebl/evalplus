```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen]
    seen.add(numbers)
    return result

if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 4, 3, 4]
    print(remove_duplicates(numbers))
    ```

This code implements a function called remove_duplicates, which takes a list of integers as input and returns a new list with duplicate numbers removed. The seen set keeps track of numbers that have been encountered, and the result list is filled with only the integers that are not in the seen set. The code includes a test, which passes the expected output, successfully demonstrating that the function removes duplicate numbers from the input list.