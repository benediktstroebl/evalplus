```python
def max_element(lst):
    if not_element(lst):
        return float('-inf')
    return max(lst, key=lambda x: x)

def not_element(lst):
    return any(x != lst[-1] for x in lst)

if __name__ == "__main__":
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
    print(max_element([1, 2, 3, 4, 5])))
    print(max_element([-5000, -3, -100, -10])))
    print(max_element([1, 2, 3, 4, 5, 6, 7, 8, 9])))
```

This code defines a max_element function that calculates the maximum element in a list. It utilizes a key argument to the `max` function, which effectively computes the maximum element while ignoring the order of elements. The `not_element` function is used to verify if the list contains at least one element that is not equal to the last element, and it returns `True`. The script then passes these functions various test cases and prints the results.