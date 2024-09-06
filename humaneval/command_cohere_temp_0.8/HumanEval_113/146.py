```python
def odd_count(lst):
    r = []
    for digits in lst:
        count = 0
        for i in range(len(digits)):
            if int(digits[i]) % 2:
                count += 1
        r.append(f"the number of odd elements in the string {count} of the input")
    return r
```

The function uses a simple loop to iterate through the list of strings and count the number of odd digits in each string. It then generates a string to fit the specification and appends it to the result list.