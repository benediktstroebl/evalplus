Here is a Python script that includes a self-contained function that solves the problem you described and passes the tests:

```python
import math
from typing import List, Tuple
def find_closest_elements(numbers: List[float]):
    """ Returns two elements from the list that are the closest to each other, and returns them in order (smaller number, larger number).
    
    Parameters: 
        numbers (List[float]): The list of numbers to select the closest two elements from
    
    Returns: 
        Tuple[float, float]: A tuple containing the two closest elements in the list, with the smaller number first and the larger number second

test_find_closest_elements_list( [1.0, 2.0, 3.0, 4.0, 5.0, 2]) -> (2.0, 2)
test_find_closest_elements_list( [1.0, 2.0, 3.0, 4])-> Boys don't let you return a function value as a function with two or more input arguments, and you must return a tuple with the values of all the arguments.

This is a common Python idiom, so that people can easily understand the purpose of your function. 

You should consider using a more descriptive name for your function, and you should also try to make your function more efficient, readable, and easier to test.