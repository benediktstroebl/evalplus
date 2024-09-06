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

The Python script defines a function `odd_count` that takes a list of lists, where each inner list represents a string of digits. It counts the number of odd digits in each string and returns a list of corresponding outputs. Each output consists of a string indicating the number of odd elements in the string with `count` replaced by the actual count of odd digits. The function iterates through each digit of each string, checking if it's odd and incrementing the count accordingly. The resulting count is then appended to the output list.

Here's an example usage of the function with a test case:
```python
test = ['1234567', '3', '11111111']
result = odd_count(test)
print(result)
```

And here's the expected output:
```
['the number of odd elements in the string 4 of the input', 'the number of odd elements in the string 1 of the input', 'the number of odd elements in the string 8 of the input']
``` 

This demonstrates that the `odd_count` function correctly solves the problem and generates the desired output.  This approach provides a clear and efficient way to solve the problem while maintaining code readability.