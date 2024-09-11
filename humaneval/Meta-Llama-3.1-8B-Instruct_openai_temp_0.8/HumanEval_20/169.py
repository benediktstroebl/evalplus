```python
from typing import List, Tuple
import heapq

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers: A list of float numbers.

    Returns:
        A tuple of two float numbers that are the closest to each other.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Use a min heap to store the numbers and their indices
    min_heap = [(numbers[0], 0)]
    
    # Iterate over the list of numbers
    for i in range(1, len(numbers)):
        # If the current number is smaller than the top of the heap, push it into the heap
        if numbers[i] < min_heap[0][0]:
            heapq.heappush(min_heap, (numbers[i], i))
        # If the current number is greater than or equal to the top of the heap, push it into the heap
        else:
            heapq.heappush(min_heap, heapq.heappop(min_heap))
            heapq.heappush(min_heap, (numbers[i], i))
    
    # The top two elements in the heap are the closest numbers
    closest_num1 = min_heap[0][0]
    closest_num2 = min_heap[1][0]
    
    # If the two closest numbers are the same, return them
    if closest_num1 == closest_num2:
        return (closest_num1, closest_num2)
    # Otherwise, find the closest numbers to the smaller of the two closest numbers
    else:
        return (min(numbers, key=lambda x:abs(x-closest_num1)), max(numbers, key=lambda x:abs(x-closest_num1)))

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```