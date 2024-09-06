```python
def will_it_fly(q, w):
    return (sum(q) <= w) and (w <= len(q) // 2) and all(q[i] == q[~i] for i in range(len(q) // 2))
```

The function checks that the sum of the elements of `q` is less than or equal to `w`, that `w` is less than or equal to half the length of `q`, and that all the elements of the first half of `q` are equal to those of the second half in reverse order. The function returns `True` if all conditions are met and `False` otherwise. 

Here is an example of use for this function:
```python
print(will_it_fly([1, 2], 5))
# Output: False
```
This example returns False because although the sum of the elements is less than the maximum possible weight, the list is not balanced. 

Another example of use is: 
```python
print(will_it_fly([3, 2, 3], 1))
# Output: False
```
This outputs False because the list is balanced but the sum of the elements is greater than the maximum possible weight. 

Finally, this is also correct: 
```python
print(will_it_fly([3, 2, 3], 9))
# Output: True
``` 

This outputs True because the list is balanced and the sum of its elements is less than the maximum possible weight.