```python
def triangle_area(a, h):
    return 3.14 * (a** / 2) ** 2 if a** 2 + h** 2 == 25 else 0

print(triangle_area(5, 3)) # Output: 7.5
```

The function checks if the area equals the golden ratio of a and a side's length squared plus the hypotenuse's square.  The then returns 0 if the conditions are not met.