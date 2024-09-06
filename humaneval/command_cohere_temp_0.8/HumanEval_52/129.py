```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compares each element with the threshold value `t`. 

Here is an example of how to use the below_threshold function:
```python
print(below_threshold([1, 2, 4, 10], 100))
print(below_threshold([1, 20, 4, 10], 5))
```
This will return:
```
True
False
```
Which is the expected output as it passes the given tests. 
If you want to test it with a different list or threshold, you can uncomment the print statements and modify them accordingly. 
You can also add more tests to this function by calling it with different lists and threshold values.