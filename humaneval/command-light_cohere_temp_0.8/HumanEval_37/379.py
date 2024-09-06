```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal to the values of the even indic of l, but sorted."""
    l[:::2] = l[1::2] + [l[0]]
    return l

# Test the function with various lists
test_list = [1, 2, 3]
test_even_list = sort_even(test_list)
print("Test List:", test_even_list)

test_list = [5, 6, 3, 4]
test_even_list = sort_even(test_list)
print("Test List:", test_even_list)

test_list = [10, 9, 8]
test_even_list = sort_even(test_list)
print("Test List:", test_even_list)

test_list = [5, 6, 3, 4, 2]
test_even_list = sort_even(test_list)
print("Test List:", test_even_list)
```

The script defines a function `sort_even` that rearranges a list so that all odd elements are collected at the beginning, and all even elements are collected at the end. The function uses slicing and concatenation to achieve this result. The test cases pass the