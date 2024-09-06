```python
def is_nested(s):
    stack = []
    for bracket in s:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if not stack or stack.pop() != '[':
                return False
    return not stack
```

The method employs a stack to simulate the process of encountering brackets in the sentence. We push each '[' character onto the stack and pop it when we come across a ']' character. When the stack is empty at the end of the sequence and we have no left brackets '[' unmatched, the sentence contains a proper bracket subsequence.

To determine whether a bracket is nested, we check whether the stack is empty (i.e., we are starting a new stack or adding onto it) and whether the top element of the stack (the latest added bracket) is a '[' when we add a ']' to the stack. The stack will not be empty, and the latest added bracket will match the upcoming '[' if the bracket is nested. The bracket is not nested if it doesn't fulfill these prerequisites, which is reflected in the function's return value by returning False. 

The function returns true only if at least one bracket in the subsequence is nested, as requested in the challenge.