```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x - 1)

# Tests
test_sort_even = []
test_items = [5, 6, 3, 4]
test_sort_even.push(test_items)
test_even = sort_even(test_items)
test_even.push([3, 6, 5, 4])
print("Test Even results:", test_even)

test_odd = []
test_items = [1, 2, 3]
test_odd.push(test_items)
test_odd = sort_even(test_items)
test_odd.push([1, 2, 3])
print("Test Odd results:", test_odd)
``` 
This code defines a function **sort_even**, which takes a list and returns a sorted list with even numbers sorted first and then odd numbers sorted second. The function uses the key argument to sort the list, which is a lambda function that returns the value of the item if it is even, and returns the value of the item minus one if it is odd. The test function creates a list of test items, and passes them to the sort_even function. The test function then returns the expected results.