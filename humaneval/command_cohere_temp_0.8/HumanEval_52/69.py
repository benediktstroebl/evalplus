```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and returns `True` if all elements are less than the input threshold `t`. 

Here's the inline tests that the function passes:
```python
>> below_threshold([1, 2, 4, 10], 100)
True
>> below_threshold([1, 20, 4, 10], 5)
False
``` 
This function is the minimal implementation to solve the problem and pass the given tests. It's concise and readable. If you're looking for more extensive examples, please let me know!