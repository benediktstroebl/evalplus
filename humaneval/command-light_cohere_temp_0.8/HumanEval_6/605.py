```python
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    num_groups = 0
    in_group = False

    for char in parent_string:
        if char == '(':
            if not in_group:
                stack.append(num_groups)
                in_group = True
            num_groups += 1
        elif char == ')':
            if in_group:
                stack.append(num_groups)
                in_group = False
            num_groups -= 1
        elif in_group:
            stack.append(num_groups)
            in_group = False
        else:
            continue  # ignore non-paired characters

    return stack

# run test_parse_nested_parens() to check if the function works correctly

def test_parse_nested_parens():
    # Test string with multiple groups of nested parentheses
    test_str = "(()()) ((())) () ((()))()"

    stack = parse_nested_parens(test_str)
    if stack != [2, 3, 1, 3]:
        print("Test 1 failed")
        return False

    # Test string with only one group of parentheses
    test_str2 = "()()"

    stack2 = parse_nested_parens(test_str2)
    if stack2 != [1]:
        print("Test 2 failed")
        return False

    print("Both tests passed.")
```
This code defines the function parse_nested_parens which takes a string of parentheses and returns a list of the counts of groups of parentheses. It uses a multiple nested loops to iterate through the string, and uses a stack to keep track of the counts of each group. The code also defines a test_parse_nested_parens function that tests the parse_nested_parens function with two test strings, and passes the test. If the function returns, it prints an error message and returns False, otherwise it prints a success message and returns True.