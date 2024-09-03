```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x + 1)

# Example usage:
l = [5, 6, 3, 4]
print("Sorted even numbers:", sort_even(l))  # [3, 6, 5, 4]

# Example usage:
l = [1, 2, 3, 4, 5]
print("Sorted even numbers:", sort_even(l))  # [1, 2, 3, 4]

```
This function takes a list l and sorts its elements in-non-increasing order. It uses theall the course in the list, if the element is even, then it's kept as it is, otherwise it's placed in the next position. The lambda function is used as the key to the sorting algorithm, ensuring that the even elements are sorted first.