```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.count()]]


# Test cases
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print("Result:", result)

numbers = [1, 2, 3, 3, 4, 3]
result = remove_duplicates(numbers)
print("Result:", result)

numbers = [1, 1, 2, 3, 4, 5, 2, 6]
result = remove_duplicates(numbers)
print("Result:", result)
``` 
The function **`remove_duplicates`** takes a list of integers **`numbers`** as input and returns a new list that contains only the unique elements. The function uses a list comprehension to filter out any duplicate elements. The function then creates a new list called **`result`** by iterating through the input list **`numbers`** and removing any duplicate elements. 

Finally, the code prints the result to the console. It is creating test cases with different lists of integers and the **`remove_duplicates`** function, and the output is the list of unique elements in each case.