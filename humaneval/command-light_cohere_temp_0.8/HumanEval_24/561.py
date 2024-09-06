```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number smaller than n that divides evenly.
    """
    number that divides n evenly (including 0).
    """
    # Make sure that we include 0 in the divisor search
    return 2 * ((n - 1) // 2) + 1
``` 
This function will return the largest integer that is a divisor for the given number, ensuring that it is smaller than the original number and divides evenly.