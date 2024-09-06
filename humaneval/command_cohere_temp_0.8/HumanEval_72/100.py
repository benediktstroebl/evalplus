```python
def will_it_fly(q, w):
    return (sum(q) <= w) and palindrome(q)

def palindrome(q):
    return q == q[::-1]
```

The `will_it_fly()` function uses the `palindrome()` function to determine if a list is a palindrome. It also checks if the sum of the list is less than or equal to a given weight. The weight is used to determine if the total weight of the object is less than the maximum possible weight for the object to fly. 

This code follows the test-driven development approach and is fitted with corresponding test cases to ensure the correctness of the function. 
```python
def test_will_it_fly():
    assert will_it_fly([3, 2, 3], 9) == True
    assert will_it_fly([1, 2], 5) == False
    assert will_it_fly([3, 2, 3], 1) == False
    assert will_it_fly([3], 5) == True
    assert will_it_fly([1, 2, 2, 1], 6) == True
    assert will_it_fly([20, 11, 22, 33, 50], 785) == False
``` 

You can incorporate this test suite into your Python environment using `pytest`, which is a testing framework for Python. 

I hope this helps! Let me know if you have any further questions.