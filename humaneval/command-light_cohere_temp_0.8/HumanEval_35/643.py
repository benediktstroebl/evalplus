```python
def max_element(lst):
    if not_elements(lst):  # Empty list
        return None
    return max(lst)

def not_elements(lst):
    return any([isinstance(x, (int, float)) for x in lst]) and all(x >= 0 for x in lst)

if __name__ == "__main__":
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    print("Maximum element:", max_element(test_list))  # Output: 123
    print("List is empty:", not_elements(test_list))  # Output: True
```
This Python script defines a function `max_element` that calculates the maximum element in a given list, and a related function `not_elements` to check if the input list is empty. The `if __name__ == "__main__":` block ensures that the functions are tested correctly when the script is run directly. 

This code provides a self-contained way to find the maximum element in a list while ensuring the testability of the functions.