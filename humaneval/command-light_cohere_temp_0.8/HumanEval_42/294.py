```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [i+1 for i in l]
    return result

# Test case 1
test_1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_2 = [6, 4, 6, 3, 4, 4, 10, 1, 124]
test_3 = [1, 2, 5, [6, 7], 5]
test_4 = [1, 2, 3, [10, 11], 4]

print("Test Case 1:")
print(test_1[:2] + test_1[2:] + test_1[3:] + test_1[-1:])
print())

print("Test Case 2:")
print(test_2[:2] + test_2[2:] + test_2[3:] + test_2[-1:])
print())

print("Test Case 3:")
print(test_3[:2] + test_3[2:] + test_3[3:])
print())

print("Test Case 4:")
print(test_4[:2] + test_4[2:] + test_4[3:] + test_4[-1:])
print())
```
The function `incr_list` takes a list `l` as input and returns a new list with the elements from the original list incremented by 1. This new list is the a for loop, adding 1 to each element in the list and the result is returned. 

This code is a good example of a self-contained function that can be run independently and does not require any additional variables to be defined.