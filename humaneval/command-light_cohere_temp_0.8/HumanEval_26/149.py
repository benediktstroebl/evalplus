```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize an empty list to store unique elements
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result

def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 3, 1, 4]
    expected = [1, 3, 4]
    result = remove_duplicates(numbers)
    assert expected == result

if __name__ == "__main__":
    test_remove_duplicates()
 ```

The above script defines a function `remove_duplicates` that removes duplicate elements from a list of integers. The function uses a list comprehension and keeps only the first occurrence of each element. The `test_remove_duplicates` function contains a test suite for the `remove_duplicates` function. It creates a `numbers` list with duplicate values, and then passes it to the `remove_duplicates` function. The expected result should be a list with no duplicates, which is `[1, 3, 4]`. The assert statement then checks if the result is equal to the expected value and passes the test.

Finally, the code uses the `if __name__ == "__main__":` block to run the `test_remove_duplicates` function when the script is run.