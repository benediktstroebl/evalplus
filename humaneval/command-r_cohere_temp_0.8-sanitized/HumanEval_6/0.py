from typing import List
def parse_nested_parens(paren_string: str) -> List[int]:
    depth_stack = []
    max_depth_stack = []
    tokens = paren_string.split()

    for token in tokens:
        if token == "(":
            depth = 1
            depth_stack.append(depth)
            max_depth_stack.append(depth)
        elif token == ")":
            depth_stack.pop()
            max_depth = max(max_depth_stack)
            max_depth_stack.append(max_depth)

    return [max(depth_stack) for depth_stack in max_depth_stack]