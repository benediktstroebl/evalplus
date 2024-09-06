```python
def is_nested(s):
    stack = []
    for i, br in enumerate(s):
        if br == '[':
            stack.append(i)
        elif br == ']':
            if not stack or stack.pop() != i - 1:
                return False
    return not stack
```

The script employs a stack to keep track of the square brackets encountered while iterating through the input string. When a '[' is encountered, it is pushed onto the stack, and when a ']' is encountered, the stack is checked. If the stack is empty or the top element of the stack does not match the expected bracket, it indicates an invalid sequence and the function returns False. Otherwise, if all brackets are correctly matched and at least one nested bracket is found, the function returns True.

Here is a more detailed explanation of how the code works:
1. The `is_nested()` function takes a string `s` as input, which contains only square brackets.
2. Initially, a stack data structure is initialized as an empty list `stack = []`. This stack will be used to keep track of the square brackets we encounter while iterating through the input string.
3. The string is iterated one character at a time using a `for` loop. The loop variable `br` represents the current character, which is either a '[' or a ']'.
4. When encountering a '[' character, it means an opening bracket has been encountered. Therefore, the index `i` of the current character is pushed onto the stack using `stack.append(i)`. This allows us to keep track of the opening brackets in the correct order.
5. When encountering a ']' character, it means a closing bracket has been encountered. The stack is checked to see if it is empty or not. If it is empty, it means there is no matching opening bracket, and the function returns `False` since the input string does not contain a valid bracket sequence.
6. If the stack is not empty, the top element of the stack is retrieved using `stack.pop()`. This top element represents the index of the matching opening bracket that we pushed earlier.
7. The index of the current ']' character is `i - 1`. This is because the loop iterates through the string characters in reverse order, and we need to match the ']' with its corresponding '['.
8. If the index of the current ']' character does not match the index of the top element in the stack, it means the current ']' does not have a matching opening bracket, and the function returns `False`.
9. If the index of the current ']' character matches the index of the top element in the stack, it means the closing bracket is correctly matched with its opening bracket, and the stack is checked again for any remaining elements. If the stack is empty, it means there is at least one nested bracket in the sequence and the function returns `True`.
10. If the stack is not empty after the above checks, it means there are unmatched opening brackets, and the function returns `False`.

The Python script provided above implements this logic, and when executed, it will correctly determine whether the input string contains at least one nested bracket sequence.