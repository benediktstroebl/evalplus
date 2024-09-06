```python
def will_it_fly(q, w):
    return (len(q) == 1 or q == q[::-1]) and sum(q) <= w
```

The function will return True if the object will fly, and False otherwise. The condition len(q) == 1 or q == q[::-1] checks if the list q is palindrome, q == q[::-1] checks if the list is equal to its reverse, and len(q) == 1 checks if the list has only one element. The other condition, sum(q) <= w, checks if the sum of the elements of q is less than or equal to the maximum possible weight w. 

```python
# TEST CASES
q1 = [1, 2]
w1 = 5

q2 = [3, 2, 3]
w2 = 1

q3 = [3, 2, 3]
w3 = 9

q4 = [3]
w4 = 5

print(will_it_fly(q1,w1))  # False
print(will_it_fly(q2,w2))  # False
print(will_it_fly(q3,w3))  # True
print(will_it_fly(q4,w4))  # True
``` 
This code snippet tests the `will_it_fly()` function with different inputs to ensure it returns the correct results according to the problem statement.