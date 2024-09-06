```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compares each element with the threshold value `t`. 

Here is an example of how to use the function:
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
```
This would return the values of True and False, respectively, which matches the given examples. 
If all elements in the list are less than the threshold, the function returns True, otherwise, it returns False. 

Please note that the function assumes that the list contains only numeric values. If the list contains non-numeric values or invalid syntax, the function may not work as expected. Gtk

Feel free to use and modify this function according to your needs. Let me know if you have any further questions!