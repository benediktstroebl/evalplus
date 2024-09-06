```python
def unique_digits(xs):
    odd = [x for x in xs if any(int(c) % 2 for c in str(x))]
    return sorted(odd)
```

The condition `any(int(c) % 2 for c in str(x))` checks whether any digit of the number `x` is odd. If so, it includes the number in the `odd` list. Finally, the function returns a sorted `odd` list. The description is inclusive of an example, expected output, and a note to emphasize the requirement of a sorted list. 

To test this function, you can use the following code:
```python
# Test the function unique_digits()
assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
assert unique_digits([152, 323, 1422, 10]) == []
```

The test suite covers multiple cases and can be expanded for further testing. The function also meets the requirement of being self-contained, as it doesn't import any external modules and instead uses native Python functionalities. 
If you wish to optimize memory usage, you may note that this problem can be solved using a single list comprehension without needing to create an intermediate 'odd' list. Feel free to ask if you'd like a optimized solution as well!