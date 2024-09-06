```python
def count_nums(arr):
    return sum(sum(map(int, str(n))) > 0 for n in arr)
```

This solution uses a powerful Python feature -- the ability to map and sum over a list of strings, as well as the ability to do this within a sum. This line:
```python
return sum(sum(map(int, str(n))) > 0 for n in arr)
```
is roughly equivalent to the more readable (but slightly slower):
```python
return sum(bool(int(str(n)[0]) < 0) for n in arr)
```
This function carefully avoids unnecessary conversions to int, and uses Python's map and sum to generate boolean values for each digit of each number, and sums these to get the final count.