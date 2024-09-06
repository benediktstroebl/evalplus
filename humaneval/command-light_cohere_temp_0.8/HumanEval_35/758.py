```python
def max_element(lst):
    if not_greater(lst) or not lst:
        return float('-inf')
    return max(lst)

def not_greater(lst):
    return sorted(lst) != lst or len(lst) > 1

if __name__ == "__main__":
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
    print(max_element([1, 2, 3, -5, 5, -3, 8, 9, 7]))
    print(max_element([1, 2, 3, -5, -6, 5, 7, 8, 9])))
    print(max_element([-5, -3, -9, -12, -4, -22, -21, -23])))
```
This script defines a function max_element that calculates and returns the maximum element in the input list lst. The not_greater function is used to test for edge cases, where the list contains no elements or is empty. The script also includes a main block with test cases for the max_element function to verify its correctness.