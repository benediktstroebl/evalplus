```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[seen:seen.
    seen.add(numbers) ]
```

# For demonstration, let's add some input numbers
numbers = [1, 2, 3, 2, 4, 3, 5]

# Call the remove_duplicates function
result = remove_duplicates(numbers)

# Print the result
print(result)  # Output: [1, 3, 4]
```
This code defines the remove_duplicates function, which takes a list of integers as input and returns a new list with duplicate elements removed. The function utilizes a set to keep track of elements seen before, and then checks each element against the current list and the seen elements to filter out duplicates. 

This is just one possible to solve this problem, and you can implement other solutions based on your preferences and requirements.