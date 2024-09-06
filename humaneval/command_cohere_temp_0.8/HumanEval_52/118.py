```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and checks if each element is less than the input threshold `t`. 

You can test the functionality of this function by calling it with different input values and verifying that it returns the expected outputs based on the problem statement.