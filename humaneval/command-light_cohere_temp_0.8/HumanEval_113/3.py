```python
def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list
    Each element i of the output should be "the number of odd elements in the string i of the input."

    # The number of odd digits in the first string
    n1 = 0
    for x in lst[0]:
        if x == int(x) % 2 == 1:
            n1 += 1

    # The number of odd elements in each string
    result = []
    for i in range(1, len(lst)):
        n = 0
        for x in lst[i]:
            if x == int(x) % 2 == 1:
                n += 1
        result.append(n1)

    return result
```
This Python code defines a function called `odd_count` that takes a list of strings as input. Each string in the string contains only digits. The function then counts the odd elements in each string and returns a list of those counts. The function uses a nested loop structure to iterate through each string and digit, checking if each digit is odd or not. The output of this function will be a list of counts of odd elements in each string. 

You can use this function with your markdown code blocks to test the problem.