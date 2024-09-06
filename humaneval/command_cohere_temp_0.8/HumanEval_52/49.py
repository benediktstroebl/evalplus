```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compares each element with the threshold value `t`. 

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

Another example where the function will return `False` is:
```python
list_ = [1, 20, 4, 10]
threshold = 5

print(below_threshold(list_, threshold))
```
This will output:
```bash
False
```
In this example, the list contains a number greater than the threshold value, so the function will return `False`. 
If you wish to test this function, you can do so inside a Jupyter Notebook or a Python file by calling the function with different input values and comparing the output with the expected results. 
If you prefer a more automated approach, you can also use a testing framework like pytest to create and run tests, which ensures your function behaves as expected. Pythonic practices and coding conventions are not explicitly required as this is a simple function, but they are typically beneficial for larger projects.] 

If you need any further adjustments, feel free to let me know!