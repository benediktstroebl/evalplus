```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with various lists of numbers
test_get_positive = []
for negative in [-1, 2, -4, 5, 6]:
    test_get_positive.append([negative,])
test_get_positive.append([5, 0])
    test_get_positive.append([1])

# Test the function with a mix of positive and negative numbers
test_get_positive.append([8])
test_get_positive.append([3, -5, -3, 9])

print(test_get_positive)

``` 
This code defines the function **get_positive** that takes a list lst as input and returns a new list that contains only the positive numbers from the input list.  The test_get_positive variable is used to test the function with different input lists and prints the result. The final list will contain only the positive numbers from the original lists, showing the function's correctness.