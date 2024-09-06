```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
The function `below_threshold` uses the `all` function to check if all the numbers in the list `l` are below the threshold `t`.  Below is a markdown code block with a sample input and output to demonstrate the functionality of the function: 
```
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
```
```
In the first example, the list contains numbers that are all less than the threshold value of 100, so the function returns True. In the second example, the list contains a number (20) that is greater than the threshold value of 5, so the function returns False. 

This problem can be solved using a list comprehension in Python in a more concise manner than the original implementation without the explicit `all` function.

```python
def below_threshold(l, t):
    return all(x < t for x in l)
```

This syntax uses a generator expression (`x < t for x in l`) in conjunction with the `all` function to achieve the same functionality.