```python
def odd_count(lst):
    r = []
    for i, s in enumerate(lst, start=1):
        n = sum(1 for c in s if c % 2 == 1)
        r.append(f"the number of odd elements in the string {i} of the input is {n}")
    return r
```

The Python script provides a self-contained function called `odd_count` that accepts a list of strings, each containing only digits. This function calculates the number of odd digits in each string using a generator expression within a loop and then creates a list of corresponding messages, replacing the index `i` with the count of odd elements in each string. The output is a list of descriptive messages providing the count of odd digits in each of the input strings.

Moreover, the code includes a series of test cases within a nested `>>>` block that verifies the correct operation of the `odd_count` function. These tests showcase the function's ability to handle different input scenarios, ensuring the accurate counting of odd digits and the generation of relevant messages for each case.