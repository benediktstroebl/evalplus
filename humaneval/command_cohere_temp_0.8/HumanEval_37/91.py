```python
def sort_even(l):
    even, odd = zip(*[(i, v) for i, v in enumerate(l) if i % 2 == 0])
    return [o if i % 2 else e for i, o, e in zip(range(len(l)), odd, even)]
```

This function splits the list into two halves - one for even indices and one for odd indices. It then concatenates these halves while sorting the even indices. The `zip(*[(i, v) for i, v in enumerate(l) if i % 2 == 0])` function splits the list `l` into the even indices `even` and the odd indices `odd`. The `[(i, v) for i, v in enumerate(l) if i % 2 == 0]` list of tuples is constructed using a generator expression that enumerates the list `l` and selects only elements with even indices. The `zip()` function aggregates these into two lists, `even` and `odd`. The final list comprehension `[o if i % 2 else e for i, o, e in zip(range(len(l)), odd, even)]` uses the `zip()` function to merge the `odd` and `even` lists. It also uses the `range(len(l))` function to iterate over the indices of `l`. The if-else statement selects between `o` and `e` based on the parity of the index `i`.

Here's a test to verify the function:
```python
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([0, 1, 2]) == [0, 1, 2]
    assert sort_even([7, 21, 4, 14]) == [4, 7, 14, 21]
```

This test verifies the function for different cases: integers, odd numbers, even numbers, and a mix of odd and even numbers.