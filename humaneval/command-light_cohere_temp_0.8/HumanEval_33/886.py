```python
def sort_third(lst):
    """Returns a list l' such that elements not divisible by three are in their correct relative order."""
    new = []
    for num in lst:
        if num % 3 != 0:
            new.append(num)
   
    return new

# Example usage:
if __name__ == "__main__":
    lst = [1, 2, 3, 6, 3, 4, 8, 9, 2]
    print("Sorted list:", end="")
    print(sort_third(lst))
```

This code defines a function `sort_third` that sorts a list lst such that elements not divisible by three are in their correct relative order. It does this by iterating through the list and adding the element to a new list if it is not divisible by three. The new list is then returned.