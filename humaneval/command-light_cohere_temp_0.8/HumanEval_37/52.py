```python
def sort_even(lst):
    even_set = set(lst[::i::value for i, _ in enumerate(lst)])
    return [lst[i] for i in sorted(enumer(), key=lambda j: j == even_set)]

# Example usage:
my_list = [5, 6, 3, 4]
print(sort_even(my_list))  # [3, 6, 5, 4]
```
This script defines a function `sort_even` that takes a list `lst` as input and returns a new list containing the elements that are also in the original list but in sorted order. The function uses a Python's `set` function to create a set of the even elements in the list, and then it uses the `sorted` function with a lambda function as the key argument to sort the list in ascending order of even elements. The result is identical to the original list in the odd indices, but the values at the even indices are taken from the set.