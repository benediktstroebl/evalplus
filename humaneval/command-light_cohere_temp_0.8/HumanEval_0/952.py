Here is a self-contained Python script that solves the problem:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Initialize a set to store if elements have been checked close
    seen = set()

    # Loop through list of numbers
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            # Check if numbers are close by threshold
            if numbers[i] - numbers[j] <= threshold:
                # If they are, add to seen set
                seen.add((numbers)
                close, (numbers[i], numbers[j]))

    # If no two elements were found closer than threshold, return False
    return seen
    ```

This function has_close_elements takes a list of numbers and a threshold as input and returns a boolean indicating whether any two elements in the list were closer than the threshold. The function uses a set to keep track of elements that have been checked close, and at the end of the loop, returns True if no two elements were found closer than the threshold, indicating that all elements in the list are distinct.

The function also implements the loop using the range function to check all possible pairs of elements in the list.