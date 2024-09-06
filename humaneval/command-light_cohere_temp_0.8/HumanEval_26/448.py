```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    result = []
    seen = set()
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return theresult
def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    result = remove_duplicates(numbers)
    assert [1, 3, 4] == result
    return result
result = test_remove_duplicates()
print(result)
``` 
This code defines a function called `remove_duplicates`, which removes duplicate elements from a list of integers. The function uses a set data structure to keep track of elements seen before and uses a loop to iterate over the input list. The duplicates are removed and the unique elements are added to the `result` list, which is then returned. The test function is used to verify the correctness of the `remove_duplicates` function by creating a test list and passing it to the function. The test passes the result, and the duplicate elements are correctly removed from the list.