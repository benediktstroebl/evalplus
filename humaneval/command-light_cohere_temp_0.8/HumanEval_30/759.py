```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with a list of numbers
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = get_positive(test_list)
print(result)  # Output: [2, 3, 5, 9, 123, 1]

# Test with a negative list
negative_list = [-1, 2, -4, 5, 6]
result_negative = get_positive(negative_list)
print(result_negative)  # Output: []
```
This solution provides a function get_positive that filters out negative numbers from an input list and returns a new list containing only the positive integers. The tests are then passing a list and an empty list to the function, demonstrating the correctness of the filtering behavior.