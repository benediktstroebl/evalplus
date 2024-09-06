```python
def sort_even(lst):
    even_set = set(lst[1:])
    odd_set = set(lst[:1])
    return [x for x in lst if x in even_set] + [x for x in lst if x in odd_set]

if __name__ == "__main__":
    # Test the function with a sample list
    test_list = [5, 6, 3, 4]
    expected = [3, 6, 5, 4]
    actual = sort_even(test_list)
    assert actual == expected
```
This code defines a Python function called sort_even, which takes a list lst as input and returns a new list lst' with certain modifications. The function creates two sets, even_set and odd_set, containing the even and odd elements of the original list, respectively. The function then loops through the elements of lst, and adds them to the appropriate set. The final result is a list of elements in lst' that are in the even_set and have a position in lst that is even, or in lst and are in the odd_set, and have a position in lst that is odd.