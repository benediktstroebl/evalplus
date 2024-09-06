```python
def max_element(lst):
    if not_element(lst) == None:
        return None
    return max(lst)

def not_element(lst):
    try:
        if lst == []:
            raise ValueError("Input list cannot be empty.")
        return max(lst)
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

# Test cases
max_test = max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
print(f"Maximum element: {max_test}")

empty_test = max_element([])
print(f"Maximum element of an empty list: {empty_test}")

single_element_test = max_element([1])
print(f"Maximum element of a single element list: {single_element_test}")

large_list = [1, 2,3,4,5,6,7,8,9,10]
print(f"Maximum element of a large list: {large_list}")
```

The above Python code defines a function `max_element` that finds the maximum element in a given list. It also includes a test cases to verify the function's behavior.