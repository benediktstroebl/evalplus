```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n):
        l[i] = l[i] + 1
    return l

# Test the function
test_incr_list = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_incr_list)
```
This code defines a function incr_list that takes a list l as input and returns a new list with elements incremented by 1. The function uses an "for" loop to iterate through each element of the input list and increments it by 1. The test_incr_list variable is used to test the function by calling the incr_list function with a list containing the test values, and the expected output is printed.

Note that this code is optimized for readability and efficiency, and it does not require additional external libraries or modules. The function is self-contained and can be easily imported and used in other scripts.