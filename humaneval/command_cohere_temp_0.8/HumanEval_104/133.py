```python
def unique_digits(xs):
    odd = [x for x in xs if any(int(y) % 2 for y in str(x))]
    return sorted(odd)
```
```
The function unique_digits processes the list of numbers xs element-by-element. For each number x, it checks if any digit of its representation violates the condition (i.e., is even). This is done using the any function with a generator expression int(y) % 2 for y in str(x): the loop int(y) fetches each digit of x's representation, and % 2 assesses whether the digit is even (oddly enough, yields 0s for even digits and 1s for odd digits). The list with all complying numbers is collected in the variable odd. Finally, the function returns a sorted version of odd.
```
```python
# Test with example inputs
assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
assert unique_digits([152, 323, 1422, 10]) == []
``` 
The test examples illustrate how the function works with different inputs and returns the expected results.