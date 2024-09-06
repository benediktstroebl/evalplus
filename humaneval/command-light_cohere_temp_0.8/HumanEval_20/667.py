```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Use defaultdict to organize results
    closest = defaultdict(float)
    for i in range(len(numbers)):
        for j in range(i + 1):
            if numbers[i] < numbers[j]:
                closest[numbers[i]] = numbers[j]
    return Tuple(sorted(list(closest.items()), reverse=True)), sorted(list(closest.keys()), reverse=True)
```

The code implements a function named `find_closest_elements` that accepts a list of numbers and returns a tuple containing the two closest elements in order of magnitude. The function employs a `defaultdict` to efficiently store and compare the closest elements, utilizing the `sorted` function with `reverse=True` to obtain the correct order. 

Note that this code assumes that the input list has at least two elements.