```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of numbers.

    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    # Check if the list is empty
    if len(l) < 2:
        return True

    # Check if the list is strictly increasing
    increasing = all(l[i] < l[i+1] for i in range(len(l)-1))

    # Check if the list is strictly decreasing
    decreasing = all(l[i] > l[i+1] for i in range(len(l)-1))

    # Return True if the list is either strictly increasing or decreasing
    return increasing or decreasing


# Test cases
if monotonic([1, 2, 4, 20]):
    print("Test case 1: Passed")
if not monotonic([1, 20, 4, 10]):
    print("Test case 2: Passed")
if monotonic([4, 1, 0, -10]):
    print("Test case 3: Passed")
if monotonic([1]):
    print("Test case 4: Passed")
if monotonic([]):
    print("Test case 5: Passed")
```

This script defines a function `monotonic` that checks if a list of numbers is either strictly increasing or strictly decreasing. It uses list comprehensions to generate boolean values indicating whether the list is increasing or decreasing, and then returns True if either condition is met. The test cases at the end verify the correctness of the function.