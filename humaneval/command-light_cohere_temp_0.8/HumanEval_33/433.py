```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    Args:
        l (list)
    Returns:
        l' (list)
    """
    l = [1, 2, 3]
    l.sort_third()
    first_ind = next((i for i, j in enumerate(l) if j%3 == 0))
    l[first_ind], l[next((i for i, j in enumerate(l) if j%3 == 0))]=l[next((i for i, j in enumerate(l) if j%3 == 0))], l[i]
    return l

#unit test
def test_sort_third():
    assert sort_third([1, 2, 3]) == [1, 2, 3]
```
This script defines a function called sort_third that sorts a list of numbers into another list, removing any numbers that are divisible by 3. The function then returns the test_sort_third to verify that the function works correctly.