```python
def max_element(lst):
    if not_element(lst) == None:
        return None
    else:
        return max(lst, key=lambda x: x)

def not_element(lst):
    if lst == []:
        return None
    elif all(map(lambda x: x == lst[0], lst)):
        return lst[0]
    else:
        return max_element(lst)

if __name__ == "__main__":
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
    print(max_element(["abc", "abcc"]))
    print(max_element([1, 2, -3, 5, 4, 6] ))
    print(max_element([1, 2, 3, 4, 5, 6, 7] ))
    print(max_element([1, 2, 3, 9, 8, 7, 5, 4] ))
```

The code defines a `max_element` function that takes a list as input and returns the maximum element in the list using the `max` function with a custom key function. The `not_element` function checks if the list is empty and returns `None` in that case. Then, the `not_element` function is used to check if the list passed to the `max_element` function is empty. The output of the script is the result of the `max_element` function, which is the maximum value of an increasing sequence of numbers.