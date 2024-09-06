Here's the self-contained Python function that finds the largest divisor of a given number n: 

```python
def largest_divisor(n: int) -> int:
    # Initialize a list of divisors up to the square root of n
    divs = [i for i in range(1, (n ** 0.25) // 2)]

    # Sort the list in descending order to find the largest divisor
    divs.sort()

   
            largest = divs[-1]

    # Return the largest divisor
    return largest
```