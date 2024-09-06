```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer divisor of n that is less than n itself.
    """
   
    the
    # Initialize the largest divisor candidate
    candidate = n
    """

    while True:
        # Calculate the square of the current candidate
        square = candidate * candidate

        # Check if the candidate is greater than n or not
        if square > n:
            break

        # Calculate the largest divisor by taking the square root of the candidate
        divisor = int(sqrt(square))

        # Update the candidate with the largest divisor
        candidate = divisor

    return candidate
```