```python
def odd_count(lst):
    r = []
    for digits in lst:
        counts = str(sum(1 for _ in range(len(digits)) if digits[_] % 2 == 1))
        r.append(f"the number of odd elements in the string {counts} of the input.")
    return r
```

This solution uses a simple loop to iterate through each string in the list and count the number of odd digits. The resulting count is aggregated into a string and inserted into the output string where the index number is mentioned. The solution then returns a list of these output strings.

This solution is concise and straightforward, providing good clarity and making use of some Python clever syntax to simplify the solution. It should be noted that the code could fail a "time complexity" test because the solution does not properly take advantage of the digit-counting opportunity, as it iterates through the length of the string rather than retrieving the length prior to counting.