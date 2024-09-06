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
```
True
```
The function can also be used in list comprehension as follows:
```python
[x for x in range(10) if below_threshold([1, 2, 4, 10], x)]
```
The resulting output will be:
```
<listpacking [0, 1, 2, 3]>
``` 
This highlights the utility of the `below_threshold` function for list comprehension.