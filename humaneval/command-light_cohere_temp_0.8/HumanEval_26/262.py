```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all elements that occur more than once in a list.
   
    :param numbers: list of integers
    :return: list of unique integers
    """
    numbers = set(numbers)
    return list(numbers)

def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 2, 3, 4, 1]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4] # Verify that duplicates are removed

def main():
    print("Removing duplicates...")
    print(test_remove_duplicates())

if __name__ == "__main__":
    main()
```

The solution is a self-contained function that accepts a list of integers and outputs a list of unique integers. The test_remove_duplicates function does the following:
1. Remove duplicates from the numbers and change the list to a set.
2 Use list from the set elements back to a list.

The test_remove_duplicates function verifies that the remove_duplicates function operates properly by asserting that the list of unique integers is equal to the expected output after the function has been applied to the input list of integers.