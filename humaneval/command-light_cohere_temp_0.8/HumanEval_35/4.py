```python
def max_element(lst):
    if not_unique(lst) == False:
        raise ValueError("Input list must contain unique elements")
    return max(lst)

def test_max_element():
    try:
        max_element([1, 2, 3])
        print("Test 1 passed")
    except ValueError as e:
        print("Test 1 failed:", e)

    try:
        max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        print("Test 2 passed")
    except ValueError as e:
        print("Test 2 failed:", e)

    try:
        max_element([5, "abc", -5, 2, -3, 3, 9, 0, 123, 1, -10])
        print("Test 3 passed")
    except ValueError as e:
        print("Test 3 failed:", e)

if __name__ == "__main__":
    test_max_element()
```
This code provides a function `max_element` that calculates the maximum element in a list, and tests it using three cases of unique elements, duplicate elements, and mixed data. It raises a positive test and gives appropriate feedback to the console.