```python
def max_element(lst):
    if not_positive(lst):
        return float('-inf')  # Return negative infinity for empty list or non-positive numbers
    elif lst == []:
        return 0  # Return 0 for an empty list
    else:
        return max(lst)  # Return the maximum element using the built-in max() function

def test_max_element():
    try:
        print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
        print("Should print:", float('inf'))
    print(max_element([1, 2, 3, -10, -20]))
    print("Should print:", 0)
    print(max_element([1, 2, 3, 4, 5]))

def not_positive(lst):
    return not bool(lst and lst[0])  # Return True for non-empty list and non-positive numbers

test_max_element()
```