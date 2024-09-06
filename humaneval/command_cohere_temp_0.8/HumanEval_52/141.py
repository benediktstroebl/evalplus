```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and compares each element against the threshold value `t`. 

Here is an example of how to use the function:
```python
print(below_threshold([1, 2, 4, 10], 100))
print(below_threshold([1, 20, 4, 10], 5))
```
This would result in the following output:
```
True
False
```
This demonstrates that the function correctly returns True if all the numbers in the list are below the threshold, and False otherwise.