```python
def odd_count(lst):
    r = []
    for digits in lst:
        count = sum(1 for d in digits if d % 2 != 0)
        r.append(f"the number of odd elements in the string {count} of the input")
    return r
```

This code solves the problem by using a generator expression to iterate over each digit in the list of strings, incrementing a counter for every odd digit encountered. Finally, the function returns a list of strings describing the number of odd digits in each string. 

You can verify the functionality of the solution by using the example tests provided in the problem statement. Adjust the list of strings in the test cases according to the expected output.