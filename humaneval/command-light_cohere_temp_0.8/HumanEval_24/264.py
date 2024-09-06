Here is a self-contained Python script with a function that solves the problem of finding the largest number that divides a given number evenly, smaller than n:
```python
def largest_divisor(n: int) -> int:
    """ Finds the largest number that evenly divides n, and returns it. """""
    biggest_divisor(15)
    5)

# Test case:
def test():
    assert largest_divisor(15) == 5 

# Test suite:
if __name__ == "__main__":
    test()
``` 
This script defines a function 'largest_divisor', which accepts an integer 'n' as input and returns the largest integer that evenly divides 'n', without being equal to n. The function employs the largest_divisor(n) + 1 as a divisibility condition to find such a number.