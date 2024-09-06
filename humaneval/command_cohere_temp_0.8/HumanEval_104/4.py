```python
def unique_digits(x):
    odd = [elem for elem in x if not any(int(d) % 2 == 0 for d in str(elem))]
    return sorted(odd)
```

The function `unique_digits` uses a list comprehension to filter out elements that have any even digits in their integer representation. The `not any()` is used to efficiently check if all digits are odd. Finally, the function returns a sorted list of these odd elements.

The following test cases prove the correctness of the function:
```python
# Test Case 1
assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

# Test Case 2
assert unique_digits([152, 323, 1422, 10]) == []
```