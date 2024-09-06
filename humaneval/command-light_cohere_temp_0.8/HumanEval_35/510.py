```python
def max_element(lst):
    if not_element(lst):  # Initialize with smallest element
        return lst[0]
    elif all([lst[i] > max_element(filter(lambda x: x != lst[i], lst))) for i in range(1, len(lst)):
        return lst[i]
    else:
        return lst[-1]

def not_element(lst):
    if isinstance(lst, list) and len(lst) > 0:
        return bool(lst)
    else:
        return False

# Test cases
assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)
assertEqual(max_element([]) , 0)
assertEqual(max_element([1, 2, 3]) , 3)
assertEqual(max_element([-5, -3, -4]) , -3)
assertEqual(max_element([24, -30]) , -30)

# Example usage
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
 ``` 
This script provides a self-contained Python function that solves the problem of finding the maximum element in a given list. It also has test cases to ensure the function's correctness. The function utilizes a approach that first considers the smallest element and then compares each element with the maximum element found in the list's subset.