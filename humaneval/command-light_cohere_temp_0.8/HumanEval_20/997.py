```python
from typing import List

def find_closest_elements(numbers: List[float]):
    if len(numbers) < 2:
        return numbers[0], numbers[0]
    else:
        return find_closest_elements(numbers[1:]), min(numbers[0] , numbers[1])

test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

test_closest_element = find_closest_elements(test_list)

print(test_closest_element)
```

This solution employs a recursive divide-and-conquer approach to identify pairs in the list that are the closest to each other. The function initially determines if the list has only one element, in which case it is the closest pair. If the list has at least two elements, the function calls itself recursively on the remaining elements of the list, excluding the first element. It then identifies the smallest number from the remaining elements and uses it to determine the second element of the pair. This process continues until it maximum number in the list is found.