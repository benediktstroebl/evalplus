```python
def will_it_fly(q, w):
    return (len(q) > 1 and 
            sum(q) <= w and 
            q == q[::-1])
```

The function will return `True` if the object `q` will fly according to the given criteria, and `False` otherwise. The criteria are that the object is a list with a length greater than 1, the sum of its elements is less than or equal to the maximum possible weight `w`, and it is a palindrome.

Here is an example of a test case that could be used to test this function:
```python
test_cases = [[1, 2, 3, 4, 3], [2, 3, 2], [1, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]]
weights = [5, 1, 3, 6]

for q, w in zip(test_cases, weights):
    assert will_it_fly(q, w), f"Expected {q} to fly but it didn't for weight {w}"
    assert not will_it_fly(q[1:], w), f"Did not expect {q} to fly but it did for weight {w}"
``` 
This would test various permutations of the list `q` and weights `w` to ensure that the function is correctly determining whether an object will fly or not. 

Let me know if you'd like me to explain any part of the code in further detail.