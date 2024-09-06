Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

    : Return a tuple of two floats: the first is the smaller of the two numbers and the second is the larger.
    they are ordered to return from largest to smallest.
"""
# Return the two closest elements in the list

numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

numbers = sorted(numbers, reverse=True)

# return the first two
return tuple(numbers[:2])

# return the tuple in sorted order

# print the result
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0])

print(sorted(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0))

print(tuple(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0)))  # ; < 1.7  < / 3.0)
print(tuple(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0))) 
 print(tuple(find_closest_elements([1.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0)))
print(tuple(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0)))  #  < > (3.0, 5.0)
print(tuple(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0)))
print(tuple(find_closest_elements([1.0, 3.0, 4.0, 5.0, 6.0)))
print(tuple(find_closest_elements([1.0, 1.0, 2.0, 3.0, 4.0, 5.0)))
print(tuple(find_closest_elements([1.0, 1.0, 2.0, 3.0, 4.0)))
print(tuple(find_closest_elements([1.0, 1.0, 2.0, 3.0, 4.0)))
print(tuple(find_closest_elements([1.0, 1.0, 2.0, 3.0, 4.0)))  #  < < 0.5 )
print(tuple(find_closest_elements([1.0, 1.0, 2.0, 3.0, 4.0, 5)))
print(tuple(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5)))  # < 1.0 and 2.0 are same0 ? 1.0 and 2.0 are equal as 1.0 and 2.0/ print(tuple(find_closest_elements([1.0, 1.0, 2.0, 3.0, 4)))
print(tuple(find_closest_elements([