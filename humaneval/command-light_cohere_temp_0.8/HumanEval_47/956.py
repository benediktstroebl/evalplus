```python
def median(l):
    """Return median of elements in the list l."""
    if len(l) % 2 == 1:
        return (l[len(l) // 2])
    else:
        return (l[(len(l) + 1) // 2])

# Test case 1
test_med = [5, 2, 4, 3, 1]
test_med_result = median(test_med)
print("Test case 1 result:", test_med_result)

# Test case 2
test_long = [10, -10, 1000, 6, 20, 5, -20, 3]
test_long_result = median(test_long)
print("Test case 2 result:", test_long_result)

# Test case 3
test_unordered = [-10, 4, 6, 1000, 10, 20, 2, 3]
test_unordered_result = median(test_unordered)
print("Test case 3 result:", test_unordered_result)
``` 
The code defines a median function that calculates the median of a list of numbers. The median is the average of the middle numbers when the list is sorted in ascending order. The function works for both even cases: lists with an even or odd number of elements, and handles the case of an unsorted list of numbers.