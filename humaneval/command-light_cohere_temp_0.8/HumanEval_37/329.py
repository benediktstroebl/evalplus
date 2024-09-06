```python
def sort_even(lst):
    return sorted(lst, key=lambda x: (x % 2, x))

#Test case
def test():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

# Test case 2
def test2():
    assert sort_even([4, 5, 6]) == [4, 5, 6]

# Test case 3
def test3():
    assert sort_even([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

# main execution point
test()
```
The function `sort_even` uses the `sorted` function along with a custom key function. The key function takes two elements as input: the modulo of the number by 2 and the original number.