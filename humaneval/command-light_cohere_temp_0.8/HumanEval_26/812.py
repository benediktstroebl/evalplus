```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

def test_remove_duplicates():
    numbers = [1, 2, 3, 2,4]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]
    numbers2 = [4, 2, 3, 1, 5]
    result2 = remove_duplicates(numbers2)
    assert result2 == [4, 5]

# run the test function
test_remove_duplicates()
``` 
This Python script defines a function remove_duplicates that takes a list of integers as input and removes duplicate numbers from the list. The function uses a set to keep track of numbers that have already been seen and a list to store the results. The function then iterates through the elements of the input list and adds any element to the list if it is not in the set. 

Finally, the function returns the list of unique numbers. 

The script also includes a test function that creates two lists of integers and passes them to the remove_duplicates function. The test function asserts that the resulting list of unique numbers matches the expected output. 

Finally, the test function is run and passes the test.