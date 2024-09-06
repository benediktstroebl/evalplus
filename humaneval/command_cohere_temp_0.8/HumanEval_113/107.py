```python
def odd_count(lst):
    r = []
    for digits in lst:
        count = 0
        for d in digits:
            if d % 2:
                count += 1
        r.append(f"the number of odd elements in the string {count} of the input")
    return r
```

This solution uses a basic loop to iterate through each string in the list and count the number of odd digits. The result is appended to the output list in the corresponding format specified in the markdown code block.

To test this, you can run the following:
```python
test = ['1234567', '3', '11111111']
print(odd_count(test))
```

The expected output is:
```
['the number of odd elements in the string 4 of the input.', 'the number of odd elements in the string 1 of the input.', 'the number of odd elements in the string 8 of the input.']
```

Let me know if you need anything else!