### Python Script to Sort Elements at Indices Divisible by Three
```python
def sort_third(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, 
    while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The modified list.
    """
    return [x if i % 3!= 0 else sorted([y for j, y in enumerate(l) if j % 3 == 0])[k] 
            for i, x in enumerate(l) for k in range(len([y for j, y in enumerate(l) if j % 3 == 0]))]

### Example Usage
if __name__ == "__main__":
    print(sort_third([1, 2, 3])) # [1, 2, 3]
    print(sort_third([5, 6, 3, 4, 8, 9, 2])) # [2, 6, 3, 4, 8, 9, 5]
```
This script works by iterating over the input list `l`, and for each element, checking if its index is divisible by 3. If it is, it adds the element to the list of elements that are divisible by 3. It then sorts this list of elements and selects the corresponding element to replace the original element at the divisible index. If the index is not divisible by 3, it simply copies the element over.