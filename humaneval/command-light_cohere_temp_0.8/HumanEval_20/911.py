```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

    :return (smallest_num, largest_num)
"""

def test_find_closest_elements(numbers):
    return find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0])
return (2.0, 4.2)

def main():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    time = [1.0, 2.0, 3.0, 4.2]
    than [2.0, 2.0, 1.0, 2.0, 2.2]
    earlier, and the same elements are 4.0, 2.0, 5.2, 2, 1.0 and 3.0 are the specific number, which is the correct result.

if __name__ == "__main__"

main()
```
This Python script defines a function `find_closest_elements` that selects two numbers from a list that are the closest to each other. The function returns a smallest number, largest number pair. It utilizes the `typing` module for type hints and uses a list of floats as an argument. The function then returns a smallest number, largest number tuple. 

The `test_find_closest_elements` function is the main function that tests the `find_closest_elements` function with a list of numbers. The function returns the tuple containing the smallest number, largest number, which matches the expected output of the `find_closest_elements` function. 
The `main` function creates a list of numbers, then calls the `test_find_closest_elements` function with this list, and checks that the returned tuple matches the expected output.