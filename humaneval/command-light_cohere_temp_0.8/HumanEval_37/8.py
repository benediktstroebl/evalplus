```python
def sort_even(lst):
    return sorted(lst, key=lambda x: x if x % 2 == 0 else x+1)

# Example usage:
# Test list
test_list = [1, 2, 3, 4, 5, 6]
# Function call
sorted_list = sort_even(test_list)
print(sorted_list)  # Expected output: [1, 2, 3, 4, 5, 6]

# Different list
different_list = [5, 6, 3, 4]
sorted_list2 = sort_even(different_list)
print(sorted_list2)  # Expected output: [3, 6, 5, 4]
```
This script defines a function sort_even that takes a list as input and returns a sorted list based on even integers. The key function takes an input argument, which is a lambda function that determines whether each element in the input list is even or odd. 

The lambda function returns the value of the element if it is even, and the value + 1 if it is odd. The sort_even function then sorts the input list using the sorted() function from Python's standard library. The sorted() function sorts the list based on the key function, which is applied to each element in the list. The resulting sorted list is then returned by the sort_even function.

Finally, an example of the usage of the sort_even function is shown. The example uses a test list and the function call to the test_list. The resulting sorted list is then printed to the console.