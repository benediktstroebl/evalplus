```python
def sort_even(l: list):
    return l[:] if all(n % 2 == 0 for n in l) else l[:] + [x for x in l if n % 2 != 0]

# Test cases
test_sort_even = []
test_sort_even.push_array([1, 2, 3])
test_sort_even.push_array([5, 6, 3, 4])
test_sort_even.push_array([2, 4, 8, 7])
test_sort_even.push_array([10, 20, 30, 40])

def test():
    print("Test cases:", end)
    print("Expected Output:", end)
    print("===" * len(test_sort_even))
    print("=" + " ".join(map(str, test_sort_even)))
    print("===" * len(test_sort_even))
    print("}")

test_sort_even = sort_even(test_sort_even)
test()
```

This script defines a function called sort_even that takes a list as an argument and returns a new list. The function first checks if all the elements in the list are even, and if so, it returns the original list. If not, it adds an new element to the end of the list, which is the first odd element. The function then returns the end.