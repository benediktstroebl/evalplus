```python
def sort_even(lst):
    even_lst = []
    odd = 0
    while len(lst) > 0:
        if lst[len(lst) // 2] >= lst[len(lst)]:
            even_lst.append(lst[len(lst) // 2])
            even = 1
        else:
            even_lst.append(lst[len(lst) // 2])
            even = 0
        lst = lst[len(lst) // 2:]
    return even_lst

# Test
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]

# Test
def test_sort_even2():
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
```

The Python script defines a function `sort_even` which takes a list `lst` as input and returns a list `even_lst` that is created by modifying the original list. The test functions `test_sort_even` and `test_sort_even2` test the `sort_even` function with different lists, and ensure that the function behaves as expected.  The output of the function is a list that only includes even numbers.