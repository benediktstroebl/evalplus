```python
def digitSum(s):
    return sum(map(int, list(filter(str.isdigit, s))))
```

The idea is to filter out the digit characters from the string using `str.isdigit`, convert them into integers using `map(int)`, and then sum them up.

### Detailed Steps:
1. Use the `str.isdigit` method to generate a boolean mask indicating whether each character is a digit or not.
2. Use the `filter()` function to retain only those characters from the original string based on the boolean mask.
3. Use the `map()` function to convert each retained character into an integer.
4. Use the `sum()` function to add up all the converted integers to get the desired result.

This approach takes care of the empty string case as well due to the inherent behavior of `filter()` and `map()` functions, which return an empty list when no element matches the criteria. Hence, the sum of such an empty list is 0.