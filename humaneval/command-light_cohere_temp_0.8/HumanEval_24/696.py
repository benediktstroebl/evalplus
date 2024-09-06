Here is a Python script that contains a self-contained function to find the largest number that divides a given number evenly: 

```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer less than n, that divides n evenly.
    """
    for i in range(1,int(n**0.5)):
        if n% i == 0:
            return i
    return -1
 ```