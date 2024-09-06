```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[seen:seen. ]

numbers = [1, 2, 3, 2, 4, 1, 3, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]
``` 
This function utilizes a set to keep track of elements encountered, then iterates through the input list and adds elements to the set if they're not already in there. After processing is entire list, the output will be a list of elements that are not in the set, ensuring uniqueness.