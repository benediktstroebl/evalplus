```python
def sort_third(lst):
    """Returns a list l' where all items that are not divisible by three are moved to the end of l'
    """
    return lst[:3] + [x for x in lst[3:] if x % 3 != 0] + lst[6:]

# Test cases
tests = [
    "Input: [1, 2, 3]
    "Output: [1, 2, 3]"
    "Input: [5, 6, 3, 4, 8, 9, 2]
    "Output: [2, 6, 3, 4, 8, 9, 5]
]

test_results = sort_third(tests)
print("Test Results:", test_results)
```
This script defines a function called sort_third, which arranges the elements of a list lst into a new list lst' such that all elements divisible by three are moved to the end. The function achieves this result by creating a new list that concatenates the first three elements of lst, followed by all elements from lst that are divisible by three, then followed by the final element from lst.