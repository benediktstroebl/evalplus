```python
def max_element(lst):
    if not_num(lst) == None:
        return None
    if len(lst) == 0:
        return lst[0]
    max_val = -inf
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

def test_max_element(test_list):
    assert max_element(test_list) == 5, "Error in function"

test_data = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_max_element(test_data)
``` 
The `max_element` function takes a list `lst` as input and returns the maximum element in the list. The function first checks if the list is empty or `None` and returns `None` in such cases. The function also checks if the list is empty and returns the first element of the list.