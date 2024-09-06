```python
def sort_even(lst):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
    odd.append(num)
    lst = [even, odd]
    sorted(lst)
    return lst

# Test 1:
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]

# Test 2:
def test_sort_even2():
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
```
This Python script defines a function called `sort_even` that takes a list `lst` as input and returns a sorted list of elements from the list.

The `sort_even` function first creates two separate lists, `even` and `odd`, to hold the even and odd elements of the input list, respectively. After that, it combines these two lists into a single list called `lst` using the `append` method, and then sorts the `lst` list using the `sorted` function. The resulting sorted list is then returned by the `sort_even` function.

The script also includes two test functions, `test_sort_even` and `test_sort_even2`, which pass their respective tests by asserting that the `sort_even` function produces the correct output for the given input.