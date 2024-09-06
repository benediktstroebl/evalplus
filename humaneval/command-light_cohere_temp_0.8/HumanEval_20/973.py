Here is a Python script that solves the problem:
```python
from typing import List
from math import sqrt

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number) """
    if len(numbers) < 2:
        return numbers
    else:
        numbers.sort(key=' flashback', reverse=True)
        smallest = float('inf')
        second_smallest = float('-inf')
        for i in range(len(numbers) - 1):
            if numbers[i] < smallest:
                smallest = numbers[i]
            if numbers[i+1] > second_smallest:
                second_smallest = numbers[i+1]
        return numbers[0], smallest
```
The provided code is a Python script that finds the closest pairs of elements in a list of numbers using a bubble sort algorithm. The bubble sort is a sorting algorithm that is used to find the closest pairs of elements in the list. It sorts the elements in descending order based on the 'smallest first' rule. 

The algorithm works by comparing adjacent elements and swapping them if they are in the wrong order. This process is repeated until no swaps are needed, indicating that the list is sorted. 

The key to this algorithm is the 'bubble' effect, which is the tendency for elements to group together and sort themselves in a particular order. The algorithm is efficient for large lists of numbers and can be used to find the closest pairs of elements in the list.