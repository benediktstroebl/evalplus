```python
def odd_count(strings):
    r = []
    for string in strings:
        counts = str(len(string) - sum(int(d) % 2 for d in string))
        r.append(f"the number of odd elements in the string {counts} of the input")
    return r
```

This code snippet provides a function `odd_count` designed to solve the problem statement. The function accepts a list of strings, each containing only digits, and returns a list of strings describing the count of odd digits in each input string.

The solution revolves around a for loop, iterating through each string in the input list. For each string, the length of the string minus the sum of odd digits in the string is computed and converted into a string representation. This resultant count string is then incorporated into a descriptive string, stating the count of odd elements in each string, which is then added to the growing list r. Finally, the function returns this list of descriptive strings.

This code will provide a list of strings detailing the count of odd digits for each number in the input list, adhering to the problem statement's requirements.