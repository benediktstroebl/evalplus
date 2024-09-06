```python
def odd_count(lst):
    r = []
    for digits in lst:
        count = sum(1 for digit in digits if digit % 2 == 1)
        r.append(f"the number of odd elements in the string {count} of the input")
    return r
```

This solution uses a simple loop to iterate through each string in the list and count the number of odd digits using a generator expression. The count is then appended to the solution list, which is returned after all strings have been processed. The tests provided for this problem will verify that the output list contains the correct string for each input list, as shown in the given examples.