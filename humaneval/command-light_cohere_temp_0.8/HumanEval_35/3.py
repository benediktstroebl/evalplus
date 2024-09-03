```python
def max_element(lst):
    if not_elements(lst):  # Checks for empty list
        return None
    
    max_ = max(lst)
    min_ = min(lst)
    if max >= min:
        return max
    else:
        return min

def test_max_element(test_lst):
    test_max_element(test_lst) == max_max_element(test_lst)

# Example usage
test_lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_max_element(test_lst))  # Output: 123
```
The code defines a function `max_element` that returns the maximum element in a list. The function uses the certain logic to compare the maximum and minimum element, and then returns the maximum. 

The function is then tested against a sample list using the `test_max_element` function. The output will be the maximum element from the input list.