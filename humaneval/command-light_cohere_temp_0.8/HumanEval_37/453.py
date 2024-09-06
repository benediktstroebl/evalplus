```python
def sort_even(lst):
    even_lst = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_lst.append(lst[i])
    return even_lst

# Test cases
test_sort_even = [
    [1, 2, 3],
    [5, 6, 3, 4],
    [10, 20, 30],
]

for test in test_sort_even:
    assert sort_even(test) == test
```