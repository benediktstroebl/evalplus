```python
def max_element(lst):
    if not_negative(lst):
        return max(lst)
    else:
        raise ValueError("Input list contains negative numbers, cannot determine a valid maximum element.")

def test_max_element():
    try:
        result = max_element([1, 2, 3])
        print("Maximum element:", result)
    except ValueError as e:
        print("Error:", str(e))
```
The code defines a function max_element that takes a list lst as input and determines the maximum element in the list. Additionally, it handles the particular scenario of negative numbers, which is not supported, and raises a ValueError.