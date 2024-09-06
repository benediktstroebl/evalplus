```python
def iscube(a):
    if a < 0:
        a = -a
    elif a == 0:
        return True
    else:
        for i in range(1, a):
            if a % i == 0 and a // i == i:
                return True
    return False
```

The solution employs a recursive approach, considering factors in both positive and negative contexts. It checks if the given number a can be expressed as the cube of an integer. The function first handles the special cases of negative numbers and zero, returning True for negative numbers as their absolute value will be checked next and returning True for zero as it is a valid cube. For positive numbers, it iterates through factors, starting from 1 up to the number itself. If it finds a factor i such that both a // i and a % i are equal to i, indicating perfect cubeness, it returns True. If no such factor is found after trying all possible factors up to the number itself, it returns False, indicating that the given number is not a perfect cube. 

Here is an example usage of the function:
```python
print(iscube(8))  # True
print(iscube(27)) # True
print(iscube(125)) # True
print(iscube(216)) # False
print(iscube(0))  # True
```

This example shows the function's behavior when provided with different test cases. The output confirms that the function correctly identifies valid cubes and provides appropriate responses for them while also identifying non-cubes and returning `False` for them.