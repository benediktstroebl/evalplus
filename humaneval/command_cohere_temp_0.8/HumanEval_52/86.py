```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 

Here is an example of how to use the function:
```python
list_ = [1, 2, 4, 10]
threshold = 100

print(below_threshold(list_, threshold))
```
This will output:
```bash
True
```
The function will return `True` because all the numbers in the list are below the threshold value of 100. 

If you change the list to include a number greater than the threshold, the function will return `False`:
```python
list_ = [1, 20, 4, 10]
threshold = 5

print(below_threshold(list_, threshold))
```
This will output:
```bash
False
```
This shows that the function correctly checks if all numbers in the list are below the threshold.