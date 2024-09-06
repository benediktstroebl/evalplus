```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers, key=lambda n: -n)

    # Find the two closest numbers
    i, j = 0, len(numbers) - 1
    while i < j:
        if numbers[i] < numbers[j]:
            i += 1
        else:
            j -= 1

    # Return the two closest numbers in order
    return numbers[i], numbers[j]

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)
```

This Python script defines a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two closest elements in the list, along with their relative order. 

The script then sorts the input list of numbers using the Python built-in sort function with a custom key function that compares numbers by absolute value. It then finds the two consecutive elements with the smallest and largest values, respectively, by iterating through the sorted list. 

Finally, it returns the two closest elements to each other, in order of their smaller and larger values.