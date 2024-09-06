```python
def solve(s):
    return ''.join(c.swapcase() if c.isalpha() else c for c in s)
```
This Python script defines a function `solve` taking one parameter `s` which performs the task as initially described in the prompt. It takes each character in the string and checks if it is alphanumeric, swapping its case and afterward incorporating it into a newly formed empty string. Or else, on the off chance that the character is special, it is appended to the string as it is. This handily empowers the desired output to be attained in a single line. Hence, this code snippet effectively tackles the problem.