```python
def max_element(lst):
    if not_element(lst) == None:
        return None
    return max(lst)

def not_element(lst):
    if isinstance(lst, list) and lst and all(isinstance(i, (int, float)) for i in lst):
        return True
    return False

if __name__ == "__main__":
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
    print(max_element(["hello", world, url]))
    print(max_element([1, 2, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10, oop]))
    print(max_element(None))
```

This code defines a function max_element that finds the maximum element in a given list. The not_element function tests whether a given input is a list and all its elements are either int or float. It returns True if all the **OPS** are found, otherwise it returns False. The function then returns the maximum value from the list.