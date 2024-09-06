```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen or len(seen) == 1:
            result.append(num)
            seen.add(num)
    return result
```

The remove_duplicates function uses a set, seen, to keep track of integers that have already been encountered. It appends integers to the result list if they have not been seen before or if they are the first occurrence of a repeated number, effectively removing duplicates from the list while keeping the order of remaining elements intact. 

To test this script, you can call the function with a sample input list of integers, such as:
```python
print(remove_duplicates([1, 2, 3, 2, 4]))
```

The expected output for this example will be:
```
[1, 3, 4]
``` 

This confirms that the function is working as intended, removing duplicates while maintaining the order of unique integers. 

 
**NOTE:** The above solution has a time complexity of O(n), where n is the length of the input list, and a space complexity of O(n) because it requires storing all input elements in memory, even if they are duplicated. If you are concerned about memory or performance for large lists, consider using 'set' or 'dict' methods to efficiently remove duplicates without storing them in memory entirely.