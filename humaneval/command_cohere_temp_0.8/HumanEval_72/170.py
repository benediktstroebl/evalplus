```python
def will_it_fly(q, w):
    return (len(q) == 1 or q == q[::-1]) and sum(q) <= w
```
The function will return True if the object will fly according to the given constraints. The function will return False otherwise. The given example tests will return the following results:
```
will_it_fly([1, 2], 5) -> False 

will_it_fly([3, 2, 3], 1) -> False

will_it_fly([3, 2, 3], 9) -> True

will_it_fly([3], 5) -> True
``` 
The function leverages the property that a list is a palindrome if it is composed of one element or if it is the same when reversed. The function also ensures that the weight of the object is less than or equal to the maximum possible weight.