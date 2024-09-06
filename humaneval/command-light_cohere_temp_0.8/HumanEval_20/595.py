Here is the solution:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # type checking
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")
    else:
        # Sort the list of numbers
        numbers.sort()
        smallest = numbers[0], numbers[1]
        largest = numbers[0]
        # Swap smallest and largest numbers
        numbers[0], numbers[1] = numbers[1], numbers[0]
        # Find the two numbers that are closest to each other
        for i in range(len(numbers)):
            if numbers[i] == smallest:
                largest = numbers[i]
                break
        if i == len(numbers) - 1:
            break
        # Return the two numbers that are closest
        return numbers[0], numbers[1]
```
This function takes a list of numbers and returns a tuple of the two closest numbers. The function first checks if the list contains at least two elements and raises an error if it doesn't. It then sorts the and swaps the smallest and largest number. It then iterates through largest number and continues until it finds the smallest number. If it has already found the smallest, it returns the two numbers. The function then uses the time complexity of O(n log(n)) and is a good choice for this problem.