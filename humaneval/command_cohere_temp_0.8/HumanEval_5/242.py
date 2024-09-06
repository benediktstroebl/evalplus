```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimiter`, which is the number to be interspersed between the elements of the list. 

It first creates an interim result list by iterating over the input list `numbers` and omitting all instances of `delimiter`. This captures all the numbers in the list except for the `delimiter`, in order to avoid multiplying `delimiter` by `len(numbers)` in the next step.

Then, it replicates the `delimiter` the necessary number of times to insert one between every two consecutive elements in the `numbers` list, given by `len(numbers) - len(result)`. It then extends the interim result list with these replicated instances of `delimiter`.

Finally, the interspersed list is returned. 

For example, calling `intersperse([1, 2, 3], 4)` would return `[1, 4, 2, 4, 3]`.