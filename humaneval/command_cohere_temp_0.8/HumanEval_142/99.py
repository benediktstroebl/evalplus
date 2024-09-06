```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```

The code uses a for loop to iterate through each index and integer in the list 'lst'. By using the modulo operator, it determines if each index is a multiple of 3 or 4. If so, it squares or cubes the integer as required. Finally, it adds the modified (or original) integer to the total 'result' and returns the sum upon completion. 

This solution is structured simply and efficiently, returning the expected results for the provided examples. Let me know if you'd like to proceed to incorporate it into your larger collection of problems or if you have any other related questions!