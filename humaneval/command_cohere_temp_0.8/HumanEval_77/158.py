```python
def iscube(a):
    # Check if the number is greater than 0 and equals to val^3
    return a > 0 and a ** 3 == int(a ** 3)
```

This function checks if the number is positive and then calculates its cube using the power function (`a ** 3`). It then checks if the calculated value equals the integer value of the cube. This happens all within the `isecube` function and does not require any imported libraries. 

The test cases provided by the problem should be sufficient to ensure the correctness of the function. Let's take one example test case as shown below:
```python
# Test case for iscube
print(isecube(1)) ==> True
```

This tests the above function with the argument 1, which should return True since 1 is a valid cube number. 

Let's run the rest of the test cases using the following code:
```python
# rest of the test cases
print(isecube(2)) ==> False
print(isecube(-1)) ==> True
print(isecube(64)) ==> True
print(isecube(0)) ==> True
print(isecube(180)) ==> False
```

This should print:
```
True
True
True
True
False
```

If this series of test cases prints out correctly, then the `isecube` function should be correct and ready for use.