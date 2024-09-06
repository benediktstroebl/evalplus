Here's a self-contained Python script with a function that solves the problem of finding the two closest elements in a list of floating-point numbers:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Returns a tuple containing the two closest elements from the input list in order of their magnitudes.
    
    Parameters: 
        numbers (List[float]): A list of numbers to be sorted.
    Returns: 
        Tuple[float, float]: A tuple containing the two closest elements.
    """
   
    for number, current_numbers in numbers:
            for neighbor, neighbor_number in zip(numbers[1:], numbers[::2]):
                if current_numbers[0] > neighbor_number:
                    current_numbers[0], current_numbers[1] = neighbor, neighbor_number
                else:
                    current_numbers[0], current_numbers[1] = number, neighbor_number
            return current_numbers

This function accepts a list of floating-point numbers and returns a tuple containing the two closest elements from the list, with the smaller number coming first. The function uses a array slicing and the zip function to iterate over the elements of the list in parallel, checking if each current element is closer to the next element. The neighbor element is found in the next portion of the list. The function returns the value of the current element, the next element, and the number of the next element, and compares the values to determine which is the closest. If the current element is larger than the neighbor, the current elements are updated with the neighbor element and the neighbor number.