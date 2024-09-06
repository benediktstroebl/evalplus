```python
def choose_num(x, y):
    max_even = max(x, y)
    floor_even = max_even - 1
    if floor_even % 2 == 0:
        return floor_even
    else:
        return -1
```

This Python script defines a function choose_num that takes two positive numbers x and y as arguments and returns the biggest even integer that falls within the range inclusive of both x and y.

To achieve this, it employs the max function to determine the maximum value of the two given inputs, x and y. This maximum value is retained in the variable max_even. Subsequently, the variable floor_even is assigned a value of max_even - 1. ThisFloorEven value represents the largest integer that is less than or equal to the maximum of x and y.

Lastly, the function examines if floor_even is even. If it is, floor_even is returned as the biggest even number within the range. Otherwise, the function returns -1 to indicate that no such even number exists in the given range. 

This approach ensures correctness and adaptability in handling the given scenario.