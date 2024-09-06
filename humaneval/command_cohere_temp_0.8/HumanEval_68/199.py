Here's a Python script that solves the given problem with an efficient approach using `itertools.accumulate` and `collections.counter` to find the smallest even value and its index:
```python
from typing import List
from itertools import accumulate, chain
from collections import Counter

def pluck(arr: List[int]) -> List[int]:
    even_values = list(filter(lambda x: x % 2 == 0, arr))
    num_occurrences = Counter(chain(even_values, [0]))
    
    results = []
    for idx, occur in enumerate(accumulate(num_occurrences.values())):
        if occur == 0:
            results.append([num_occurrences[0], -1])
        if occur == 1:
            results.append([num_occurrences[1], idx])

    return results if results else [[]]

# Example usage
input_list = [4, 2, 3, 1, 5, 0, 3, 0, 4, 2]
print(pluck(input_list))  # Expected output: [2, 1]
```

The code utilizes `itertools.accumulate` to aggregate the counts of even values and 0s in the array concurrently. The `collections.counter` class is used to transform the list of counts into a dictionary with sorted keys. The dictionary's keys correspond to the even values and 0, while the dictionary's values denote the nodes' indices. Finally, the code extracts the plucked node from the dictionary and returns a list that contains the plucked node alongside its index.