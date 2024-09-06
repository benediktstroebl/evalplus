```python
def max_element(lst):
    if not_positive(lst):  # Check for positive elements
        return max(lst)  # Use built-in max() function for positive lists
    else:
        return max(reduce(lambda x, y: x if x > y else y, lst, []), 0))  # Use reduce with a lambda function

def test():
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    print("Maximum element:", max_element(lst))
    lst.test = [input = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    print("Maximum element:", max_element(lst))

def not_positive(lst):
    return all(x > 0 for x in lst)
```
The provided code defines a function `max_element` that computes the maximum element in a list, considering both positive and negative values. The `test` function creates a test list and demonstrates the functionality by finding the maximum element using the `max_element` function. The code also has a `not_positive` function to check if the input list contains only positive elements.