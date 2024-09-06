Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Initialise list to [0,0,0]
    result = [0.0, 0.0, 0.0]
    
    # numbers[numbers]
    total = len(numbers)
    
    # Create a list of zeros with length total
    zeros = [0] * total
    
    # Use the list comprehension to populate zeros list with numbers from numbers list
    zeros[:total // 2] = numbers[:total // 2]
    
    # Add the same number to every element in the list
    for i in range(total // 2):
        zeros[i] += numbers[i]
    
    # Calculate the maximum number in the list
    mx = max(numbers)
    
    # Apply the formula
    for i in range(total // 2):
        result[i] = result[i] / (zeros[i] + 1e - 1) / mx
    
    # Return the new list
    return result

# Example 
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

result = rescale_to_unit(numbers)

Note that this solution will be a list [0.0, 0.0, 0] because the smallest number will become 0 and the largest number will become 1.