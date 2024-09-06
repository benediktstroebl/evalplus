```python
def max_element(lst):
    if not_numbers(lst):
        return "Input list is empty or contains only numbers"
    return max(lst)

def not_numbers(lst):
    return any(n for n in lst if n <= 0)

if __name__ == "__main__":
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5]) == 3
    assert max_element([-5, -3, 3, -10, 0, 9, 2]) == 123
    assert max_element([5, 0, -10, -3, 3, 9]) == -3
    assert max_element([-1, -10, 100, -3]) == -10
```
The provided Python script defines a function max_element that aims to find the maximum element in a given list. The function first checks if the the input list is empty or contains only numbers, and in that case, it returns an error message. The function then uses the maximum function to find the maximum element in the list, and returns the result.