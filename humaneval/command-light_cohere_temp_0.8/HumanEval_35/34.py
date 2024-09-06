```python
def max_element(lst):
    if not_elements(lst):
        return None  # Empty list, return None
    if not_positive(lst):
        return lst[0]  # Return first positive number as max
    for num in lst:
        if num > max_element(filter(lambda x: x > num, lst))[0]:
            max_element = num
    return max_element

def not_elements(lst):
    return all(x > 0 for x in lst)

def not_positive(lst):
    return all(x > 0 for x in lst)

if __name__ == "__main__":
    print(max_element([1, 2, 3]))
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```
The provided Python script defines a function `max_element` that calculates and returns the maximum element from a given list. The `not_elements` and `not_positive` helper functions are used to ensure that the input list is valid and contains positive numbers before invoking the `max_element` function. The `__main__` section includes sample test cases for the `max_element` function, showcasing its functionality.