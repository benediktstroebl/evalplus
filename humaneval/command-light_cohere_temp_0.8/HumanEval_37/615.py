```python
def sort_even(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted."""
    return lst[:-2] + lst[2:];

# Example usage:
if __name__ == "__main__":
    lst = [1, 2, 3]
    print("Sorted even list:", end=" ")
    print(sort_even(lst))
```
The function takes a list lst and returns a list lst' which is identical to lst in the odd index, while its values at the even index are equal to the values of the even index of lst, but sorted.