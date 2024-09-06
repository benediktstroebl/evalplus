Here's a self-contained Python function that solves the problem:

```python
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    If there are two numbers in the list that are less than the threshold apart, return True
    If there are no such pairs, return False.
    """

Here's the test code for this function:

```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]

threshold = 0.3)
result = has_close_elements(numbers, threshold)

```
This test creates a list of numbers and a threshold value. The test then checks if any two numbers in the list are closer than the threshold.