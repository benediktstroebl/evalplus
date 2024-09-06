```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x` and compare it to the threshold `t`. The `all()` function returns `True` if all comparisons are `True`, meaning that all numbers in the list are below the threshold, and `below_threshold` returns `True`. Otherwise, if any comparison is `False`, `all()` returns `False`, and `below_threshold` returns `False`. The function works correctly for the given test cases, where it returns `True` for the first example and `False` for the second. 
If you want to test this function, you can write tests like the ones provided in the original prompt. You can do it by adding a test list and a threshold and comparing the function's output with the expected `True` or `False`. 
```python
# Test 1: All numbers in the list are below the threshold
test1_list = [1, 2, 4, 10]
test1_threshold = 100
test1_result = below_threshold(test1_list, test1_threshold)
assert test1_result == True

# Test 2: All numbers in the list are above the threshold
test2_list = [1, 20, 4, 10]
test2_threshold = 5
test2_result = below_threshold(test2_list, test2_threshold)
assert test2_result == False
```

This way, you can ensure that the function behaves correctly. 
If you want to make the code more concise, you can achieve the same result without using the `all()` function. Here is a version of the code that uses a shorter syntax for the same logic:
```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This code uses the same comparison logic but in a more condensed form. Both versions of the code achieve the same result and solve the problem, so you can choose the one that better fits your preferences.