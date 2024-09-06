def match_parens(lst):
    def shift_left(stack, curr):
        # If stack is empty or the top element is different from curr, push curr to stack
        if not stack or stack[-1] != curr:
            stack.append(curr)
            return True    
        # If stack top is curr, do nothing and return False
        return False

    def shift_right(stack, curr):
        # If stack is empty or the top element is different from curr, push curr to stack
        if not stack or stack[-1] != curr:
            stack.append(curr)
            return True
        # If stack top is curr, do nothing and return False
        return False

    # Example of stack: ['(', '(', ')', '(', ')', '(']
    stack = []
    for char in lst[0]:
        if char == '(':
            shift_left(stack, char)
        else:
            shift_right(stack, char)
    # Example of stack after processing the first string: ['(', '(', ')', '(', ')']

    for char in lst[1]:
        if char == '(':
            shift_right(stack, char)
        else:
            shift_left(stack, char)
    # Example of stack after processing both strings: ['(', ')']

    if len(stack) == 0:
        return "Yes"
    else:
        return "No"