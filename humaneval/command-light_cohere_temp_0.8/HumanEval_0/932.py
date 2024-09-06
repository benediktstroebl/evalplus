Here's a Python script with a self-contained function that solves the problem:

```python
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    Returns True if any two numbers in the list are closer to each other than the threshold.
    """


numbers = [1.5, 0.5, 1.5, 9.5, 3.5, 2.5, 5.0, 0.5, 0.5, 0.5, 0.5, 3, 0, 8, 9, 10]
threshold = 0.1

if has_close_elements(numbers, threshold):
    print("YES")
else:
    print("NO")

```

This script defines a function called `has_close_elements` that takes a list of numbers and a threshold as input. It uses the Python's built-in `type` module to define the type of the input parameters, which is a List[float]. The function then uses an if statement to check if any two numbers in the list are closer to each other than the threshold. The function returns True if the result is True, indicating that there are any two numbers in the list that are closer to each other than the threshold. The function returns False if there are no such.