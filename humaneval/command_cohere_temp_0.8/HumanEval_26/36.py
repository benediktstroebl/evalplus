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

The approach used is a mixture of set and list manipulation. A set `seen` is used to keep track of all already encountered elements in the input list. A list `result` is used to store the unique elements in the order they appear in the input list. 

For each integer `num` in the input list `numbers`, the following checks are performed:
- If `num` has not been encountered before (`num not in seen`), it is added to both the set `seen` and the list `result`.   
- If `num` has already been encountered once (`len(seen) == 1`) and therefore will be removed from the list by the uniqueness constraint, it is only added to the `result` list. 

In this way, the element `num` is either added to or removed from the output list based on the uniqueness constraint, while still maintaining the original order. 

Such an approach requires linear amounts of memory for the output list and the set, and also has a time complexity of O(n), where n is the number of elements in the input list. 

The code is also safe against potential data loss due to the `seen` set not being sufficiently large enough to hold unique elements. By only adding elements that are encountered at least once in the input list, the `seen` set will never grow larger than the size of the input list. 

This is also an efficient solution, as the list-based `result` stores elements in the same order as the input, and the set-based `seen` only stores unique elements from the input list. 

These properties ensure that the function is both safe and efficient in solving the given problem. 

This approach is efficient compared to brute-force solutions that use `sorted()` and `list.remove()` methods, as those solutions require O(n log n) time complexity and higher amounts of memory. 

Let me know if you would like me to explain any of the details of the solution in more detail.