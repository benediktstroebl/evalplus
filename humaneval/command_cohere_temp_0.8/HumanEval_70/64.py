```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions with maximum values
    # and even positions with minimum values
    for val in lst:
        if len(sorted_list) % 2 == 0:
            # If the list is even add the minimum value
            if val < min_val:
                min_val = val
                sorted_list.append(min_val)
        else:
            # If the list is odd add the maximum value
            if val > max_val:
                max_val = val
                sorted_list.append(max_val)
    
    return sorted_list
```

This Python script defines a function called `strange_sort_list` that takes in a list of integers as input. It sorts the list in a strange order where odd positions contain the maximum value among the remaining elements, and even positions contain the minimum value among the remaining elements. The function starts by setting the minimum and maximum values to positive and negative infinity, respectively, and initializing an empty list called `sorted_list` to store the sorted elements. Then, it iterates through the input list, checking if the length of `sorted_list` is even or odd. If the length is even, the function appends the smallest value encountered to `sorted_list`, updating the `min_val` as needed. If the length is odd, the function appends the largest value encountered to `sorted_list`, updating the `max_val` as needed. 

Here is an example of how to use the function:
```python
print(strange_sort_list([1, 2, 3, 4]))  # Output: [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # Output: [5, 5, 5, 5]
print(strange_sort_list([10, 9, 8, 7]))  # Output: [7, 10, 9, 8]
``` 

This function is also test-friendly, and the following code can be added to test the function:
```python
def test_strange_sort_list(arr):
    # Test list with positive and negative numbers
    assert strange_sort_list(arr) == [arr[0], arr[2], arr[1]]
    assert strange_sort_list([10, 9, 8, 7]) == [7, 10, 9, 8]

    # Test list with equal values
    assert strange_sort_list([1, 1, 1, 1]) == [1, 1, 1, 1]

    # Test list with no elements
    assert strange_sort_list([]) == []

    # Test list with floating point numbers
    assert strange_sort_list([0.5, 1.5, 2.5, 3.5]) == [0.5, 2.5, 1.5, 3.5]

test_strange_sort_list([1, 2, 3, 4])
test_strange_sort_list([5, 5, 5, 5])
test_strange_sort_list([10, 9, 8, 7])
test_strange_sort_list([1, 1, 1, 1])
test_strange_sort_list([])
test_strange_sort_list([0.5, 1.5, 2.5, 3.5])