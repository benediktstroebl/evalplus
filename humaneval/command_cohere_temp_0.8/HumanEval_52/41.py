```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
This function uses the built-in `all` function to return True if all elements in the list `l` are below the threshold `t`. 

Here is an example of how to use this function:
```python
print(below_threshold([1, 2, 4, 10], 100))
```
This will return:
```bash
True
```
The function can also be used in a more compact manner:
```python
print(below_threshold([1, 20, 4, 10], 5))
```
which will return:
```bash
False
```
Please note that the function assumes that the list contains numbers and the threshold is a number as well. If the list or the threshold is of a different type, the function may not behave as expected.