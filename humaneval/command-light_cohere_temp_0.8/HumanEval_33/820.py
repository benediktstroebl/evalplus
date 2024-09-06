```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 1, 2, 3, 4, 5])
    Traceback (most recent call last):
      File "<string>", line 3, in <module>
        raise ValueError("Unsupported input types")
    ValueError: Unsupported input types
```
The function raises an error if the list contains elements of an unsupported type. 
It returns a list of lists, where each inner list contains elements that are not divisible by three, and elements that are divisible by three are equal to the corresponding elements in the original list, but sorted.