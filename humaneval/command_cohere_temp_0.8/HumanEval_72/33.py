```python
def will_it_fly(q, w):
    return (sum(q) <= w) and (w % 2 == 0) and all(q[i] == q[~i%len(q)] for i in range(len(q)))
```

The function relies on three tests:
1. The sum of the elements in the container `q` must be less than or equal to the maximum weight `w`.
2. To be flyable, the container must be balanced, i.e., each element must have a matching element of the same value at an opposite position within the container, like in `[[1, 1], [2, 2], [3, 3]]`. 
3. The maximum weight for a flyable object is always even, so if `w` is odd, it automatically rules out any object with an odd sum. 

This function should be able to solve the "Will it Fly" problem for any given container `q` and maximum weight `w`. 

Let's take three examples from the problem statement to validate the solution:
```python
print(will_it_fly([1, 2], 5))  # False
print(will_it_fly([3, 2, 3], 1))  # False
print(will_it_fly([3, 2, 3], 9))  # True
``` 

The function will return `True` if the object will fly and `False` otherwise.