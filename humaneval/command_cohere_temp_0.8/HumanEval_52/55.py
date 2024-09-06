```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x`, comparing it to the threshold `t` using the `<` operator. The `all()` function returns `True` if all comparisons are `True`, indicating that all numbers in the list are below the threshold, otherwise `False`. 

Here is a test case to ensure the function runs correctly:
```python
assert below_threshold([1, 2, 4, 10], 100), "Expected True, but got False"
assert not below_threshold([1, 20, 4, 10], 5), "Expected False, but got True"
```
These test cases assert that the `below_threshold()` function returns `True` when all elements in the list are below the threshold and `False` otherwise. 
The function passes the provided tests and solves the problem correctly. 
It handles the edge cases and behaves as expected. 
It can be further improved to handle additional edge cases and follow best practices to handle this specific problem and be more generally applicable. Might that be something you are interested in?