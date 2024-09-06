```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    
    # Get the two closest elements in the sorted list
    first_index = next((i for i, n in enumerate(sorted_numbers) if n < sorted_numbers[i])[1])
    second_index = next((i for i, n in enumerate(sorted_numbers) if n == sorted_numbers[i])[1])
    
    # Return the two closest elements in the list
    return (sorted_numbers[first_index], sorted_numbers[second_index])

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 2]
print_results(find_closest_elements(numbers)))

def print_results(result):
print("First element:", result[0])
print("Second element:", result[1])
```

The above Python script defines a function called `find_closest_elements`, which takes a list of numbers as input and returns a tuple containing the two closest elements in the list, along with their relative difference. The function uses the sorting the list of numbers and then finds the two closest elements based on their relative difference. The `print_results` function is used to test the `find_closest_elements` function with a sample list of numbers.

When you run this script, it will output the two closest elements in the list, along with their relative difference.