```python
def sort_even(lst):
    even = [x for x in lst if x % 2 == 0]
    return even + [x for x in lst if x % 2 != 0]

# Test case: pass list with elements of both even and odd
#    numbers.
print(sort_even([1, 2, 3]))
# Expected output: [1, 2, 3]

# Test case: list with even and odd numbers mixed
print(sort_even([5, 6, 3, 4]))
# Expected output: [3, 6, 5, 4]
```
The function returns a list containing the elements of the original list, but with the even numbers sorted to the front. The function also handles the basic cases of lists with even and odd numbers. The tests cover a scenario of sorting lists with even and odd elements, as well as lists with even and odd numbers mixed together.