```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x` and compare it to the threshold `t`. The `all()` function returns `True` if all comparisons are `True` and `False` otherwise, returning the overall conclusion about the list being below the threshold. 

Here is a test case for this function:
```python
assert below_threshold([1, 2, 4, 10], 100) == True
```
```markdown
This should evaluate as True since all numbers in the list are below the threshold of 100.
``` 

And here is another test case:
```python
assert below_threshold([1, 20, 4, 10], 5) == False
```
```markdown
This should evaluate as False since one of the numbers (20) is above the threshold of 5. 
``` 
This provides a correct and concise solution to the problem.