from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    open_stack = []
    close_stack = []
    current_group = []
    output = []

    for char in paren_string:
        if char == '(':
            open_stack.append(char)
        elif char == ')':
            close_stack.append(char)
            if not open_stack:
                print("Unmatched close parenthesis")
                return []
            open_stack.pop()
            current_group.append(char)

        # If the current open bracket opened earlier in the string, add it to the current group and move on
        while open_stack and open_stack[-1] == current_group[0]:
            open_stack.pop()
            current_group.insert(0, open_stack.pop())

        if not open_stack:
            output.append(''.join(current_group))
            current_group = []

    # Close whatever brackets are left in the open stack
    while open_stack:
        output.append('')
        for _ in range(len(open_stack)):
            close_stack.append(open_stack.pop())

    return output
paren_string = '( ) (( )) (( )( ))'