```python
def triangle_area(a, b, c):
    s = lambda x, y: x + y - c
    return round(0.5 * np.sqrt(max(s(a, b), s(b, c), s(c, a))), 2) if max(s(a, b), s(b, c), s(c, a)) else -1
```

This Python script defines a function 'triangle_area' that takes in three parameters, 'a', 'b', and 'c', representing the lengths of the three sides of a triangle. The function first uses a lambda function 's' to calculate the difference between the sum of any two sides and the third side. It then uses the numpy 'sqrt' function to calculate the square root of the largest difference among these three calculations. It multiplies this result by 0.5 to get the area of the triangle. If the sum of any two sides is not greater than the third side, the function returns -1 to indicate an invalid triangle. 

The function uses the 'round' function to round the calculated area to two decimal places for precision. 

Please note that this code assumes that the numpy library has been installed, as it requires the use of the 'np' module. You can install numpy like so:
```bash
pip install numpy
``` 

To do so, you can add a import statement at the beginning of the script:
```python
import numpy as np
```

This will enable the use of numpy within the script.