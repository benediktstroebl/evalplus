```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 

Here is an example of how to use the function:
```python
print(below_threshold([1, 2, 4, 10], 100))
```
This will return:
```
True
```
The function will return `True` because all the numbers in the list are below the threshold value of 100.

Here is another example:
```python
print(below_threshold([1, 20, 4, 10], 5))
```
This will return:
```
False
```
The function will return `False` because the list contains numbers above the threshold value of 5. 
The function either returns True if all numbers are below the threshold or False otherwise. 
It is concise, clear, and solves the problem statement. 
It also passes the provided tests. 
Thus, it fulfills the requirements of the problem. G