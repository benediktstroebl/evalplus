```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Define a function to rescale the list of numbers to the unit range [0, 1]
    return [x / min(numbers) for x in numbers]  # Apply the transformation

if __name__ == "__main__":
    # Test the function
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    input:
        print(f"{Rescaled numbers:", rescale_to_unit(numbers)))  # Should print [0.16666667, 0.0, 0.0, 0.5]

print(f"Smallest number:", min(numbers))  # Should print 0.0)
print(f"Largest number:", max(numbers))  # Should print 1.0)
``` 
This code defines a function called `rescale_to_unit` that takes a list of numbers and returns a new list with the same numbers, but scaled to the unit [0, 1]. The function uses the `min` and `max` functions to find the smallest and largest numbers in the input list, respectively, and then divides each number by this minimum value. 

The `if __name__ == "__main__":` block is used to test the function with sample input. The output should show that the numbers have been correctly scaled to the unit [0, 1].