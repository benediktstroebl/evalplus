```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code uses the built-in Python `map` function to convert the string representation of apple and orange quantities (`s.split(' and ')` provides a list of strings) into integer values. Then, the total quantity of the mango fruits in the basket is computed as the difference between the total number of fruits (`n`) and the sum of the apples and oranges. To handle scenarios where there might be leading zeros in the string (e.g., "0 apples"), the code ignores such leading zeros during the calculation. 

This solution assumes that "mango fruits" are not mentioned in the input string, which is a reasonable assumption based on the problem statement. If the quantity of "mango fruits" was mentioned in the input alongside apples and oranges, a different approach would be needed.