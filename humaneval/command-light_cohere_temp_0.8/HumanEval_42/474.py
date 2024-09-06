```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n):
        l[i] += 1
    return l

# Test the function with a range of inputs
for i in range(0,10):
    test_list = incr_list([i])
    print(test_list)
``` 
This Python function, `incr_list`, takes a list as input and returns a new list with elements incremented by 1. The function uses a range-based loop to iterate through each element in the input list and increments it by 1. This results in a list with the elements being one step higher than the original list. The function is then tested with a range of inputs, and the output is printed to the console.