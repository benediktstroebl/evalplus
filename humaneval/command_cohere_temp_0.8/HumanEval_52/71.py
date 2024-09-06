```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 

Here is an example of how to use the function:
```python
print(below_threshold([1, 2, 4, 10], 100))
```
This will output:
```bash
True
```
The function will return `True` because all numbers in the list `[1, 2, 4, 10]` are below the threshold value of `100`.

Here is another example:
```python
print(below_threshold([1, 20, 4, 10], 5))
```
This will output:
```bash
False
```
In this example, the list contains a number `20` that is above the threshold value of `5`, so the function will return `False`. 

The function fully adheres to the problem statement and test scenarios outlined in the original prompt, as demonstrated by these examples.