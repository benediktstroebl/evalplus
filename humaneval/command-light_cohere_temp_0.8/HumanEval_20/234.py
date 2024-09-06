Here is a self-contained Python script that solves the problem of finding the closest elements in a list of numbers:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # initialize a tuple of (smaller, larger) values
    smaller, larger = (numbers[0], numbers[1])

    # Initialize two pointers, i and j, which will be used to traverse the list
    i = 0
    j = 1

    # The loop iterates as long as the two values in the tuple do not have the same sign
    while i < len(numbers) - 1 and j < len(numbers) - 1:
        if numbers[i] != numbers[j]:
            # if the smaller value is positive, move the pointer i forward
            if smaller > numbers[i]:
                i += 1
            # if the smaller value is negative, move the pointer j forward
            else:
                j += 1
        # The loop terminates when both values have the same sign, or when one of them has reached the end of the list
        if numbers[i] < numbers[j] or j == len(numbers) - 1:
            # At this point, the largest value is at the end of the list, so reverse the order of the two values in the tuple
            smaller, larger = larger, smaller
            # Return the two values in order of the tuple
            return smaller, larger
    else:
        # Move the pointer i forward to the next value in the list
        i += 1
    return larger
```

This function, named `find_closest_elements`, takes a list of numbers as its argument and returns a tuple containing the two elements that are closest to each other. It uses a the initializes two pointers, `i` and `j`, which are used to traverse the list. Then, the loop iterates as long as the two values in the tuple do not have the same sign, and until the two values have the same sign or until one of them has reached the end of the list. The function then swaps the values in the tuple and returns the tuple.