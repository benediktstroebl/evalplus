```python
def median(l: list):
    """Return median of elements in the list l."""
    return (len(l) + 1) / 2 * (sorted((l[::i // 2] for i, ::(len(l) - 1)))[0])

#Test 1: Test a function with an empty list
assert(median([]) == 0)

#Test 2: Test a function with a list with only one element
assert(median([1]) == 1)

#Test 3: Test a function with a list with odd length
assert(median([1, 2, 3]) == 2)

#Test 4: Test a function with a list with even length
assert(median([1, 2, 4, 5])) == 5

#Test 5: Test with negative numbers
assert(median([-10, 4, 6, 1000, 10, 20])) == 15)

#Test 6: Test with large numbers
assert(median([1000, 100, 10])) == 10
```