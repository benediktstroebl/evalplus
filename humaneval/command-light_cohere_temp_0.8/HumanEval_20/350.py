Here is a self-contained Python script that solves the problem you've described:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers, key=lambda x: x)
    # Find the two closest elements and return them in order
    # (i.e., the smaller number, larger number)
    for i in range(1, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                # Swap numbers[i] and numbers[j]
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers[0], numbers[1]
```

The function 'find_closest_elements' takes a list of numbers as input and returns a tuple containing the two closest numbers in the list, which are returned in ascending order.

This function uses the 'typing' module to help ensure type safety and allows the function to take any type of input.

It sorts the list of numbers using the built-in method 'sort()' and then uses two nested loops to find the two closest elements in the list. The outer loop finds the smallest number, and the inner loop finds the larger number. The two numbers are then swapped using the 'swap()' method, and then returned in order.