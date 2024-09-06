```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and compare it to the threshold value `t`. The `all` function returns `True` if all iterated elements are true, and `False` otherwise. 

This solution is concise and straightforward, letting the built-in `all` function do most of the work. It easily passes the given tests:
```python
> below_threshold([1, 2, 4, 10], 100)
True
> below_threshold([1, 20, 4, 10], 5)
False
``` 
It is good practice to use built-in functions like `all` when possible, and your solution is clear and efficient. This allows for easy understanding and maintenance of the code.