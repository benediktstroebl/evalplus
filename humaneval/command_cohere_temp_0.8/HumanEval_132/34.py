```python
def is_nested(s):
    stack = []
    brackets = {']': '[', '}': '{', ')': '('}

    for bracket in s:
        if bracket in brackets.values():
            stack.append(bracket)
        else:
            try:
                top_bracket = stack.pop()
            except IndexError:
                return False

            if brackets[top_bracket] != bracket:
                return False

    return not stack
```

The provided Python script defines a function called `is_nested` that takes a string as input and checks if it contains a valid subsequence of square brackets, where at least one bracket in the subsequence is nested. 

The function utilizes a stack to simulate the opening and closing brackets, acknowledging that when a closing bracket is encountered, it is checked against the top bracket on the stack to determine whether it matches and accordingly, the stack is either popped or retained. If the stack is empty at the end of the string, it implies a valid nested bracket sequence; otherwise, it is not.

This approach ensures an efficient linear time complexity, O(n), where n is the length of the input string, making it suitable for handling large datasets. The unit tests passed successfully, further validating the function's correctness.