```python
def starts_one_ends(n):
    return sum(str(x)[:n] == '1' or str(x)[:-n] == '1' for x in range(10, 10**n + 10, 2))
```
This function:
- Creates a generator function that iterates through the numbers between 10 and 10^n, skipping every second number.
- For each number in this sequence, it checks if its first n digits or last n digits are '1'. This is done using the str(x)[:n] and str(x)[:-n] techniques.
- Filters out the numbers that satisfy either of these conditions.
- Returns the count of such numbers. 

This approach ensures that the time complexity is O(n) and the count of numbers starting or ending with 1 can be computed in a straightforward manner.