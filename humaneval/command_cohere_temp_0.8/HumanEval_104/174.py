```python
def unique_digits(xs):
    result = [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
    return sorted(result)
```
This Python script defines a function `unique_digits` that solves the problem as outlined in the markdown code block. It takes a list of positive integers `xs` as input and returns a sorted list of elements that do not contain any even digits. The function uses a list comprehension to filter out elements that have at least one odd digit, and then sorts the resulting list in increasing order. 

Here is an example of how you can use the code:
```python
test_list = [15, 33, 1422, 1, 152, 323, 1422, 10]
print(unique_digits(test_list))  # Output: [1, 15, 33]
```

This would output the expected result of the function, which is [1, 15, 33]. 

Is there anything else I can help you with? Let me know if you'd like me to assist with additional code problems or clarification on any concepts!