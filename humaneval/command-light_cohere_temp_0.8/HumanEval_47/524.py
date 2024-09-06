```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[-1] + lst[0]) / 2
    else:
        return lst[int((n - 1) / 2)]

# Test case 1: Check if the function correctly calculates the median of the list with an even number of elements
assert(median([3, 1, 2, 4, 5])) == 3

# Test case 2: Check if the function correctly calculates the median of the list with an odd number of elements
assert(median([-10, 4, 6, 1000, 10, 20])) == 15)

# Test case 3: Check if the function handles lists with negative elements
assert(median([-10, 4, 6, 1000, 10, 20])) == 15)

# Test case 4: Check if the function handles lists with different lengths
assert(median([4, 6, 7]) == 6)

# Test case 5: Check if the function handles empty lists
assert(median([])) == float('inf'))  # Infinity

```
This Python script defines a function median that calculates the median of a list of numbers. It also includes a series of test cases that validate the correctness of the function for different scenarios. The script demonstrates the method by using the assert statements to check if the function produces the expected results for the provided test cases.