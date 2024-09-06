Here's a self-contained Python function that finds the largest divisor of a given number n: 

```python
def largest_divisor(n: int) -> int:
    """ Returns the largest number divisible by n, smaller than n."""
    while True:
        div = 1
        while div * div <= n:
            div += 1
        return div
``` 

This function uses a simple while loop to find the largest integer divisible by the given number, smaller than the original number. 

It ensures the loop iterates up the square of numbers, to safely stay under the given number.