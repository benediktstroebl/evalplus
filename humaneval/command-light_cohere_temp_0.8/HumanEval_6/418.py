Here is a self-contained Python script that solves the problem you described:
```python
def parse_nested_parens(parenthesis_string: str) -> List[int]:
    stack = []
    result = []
    i = 0

    while i < len(parenthesis_string):
        char = parenthesis_string[i]
        if char == "(":
            stack.append(1)  # Start new group
        elif char == ")":
            if not or stack == []:
                result.append(3)  # End of the group with no nesting
            stack.pop()
        elif stack:
                stack[-1] += 1  # Add to the top of the stack
        else:
            result.append(2)  # End of the group with two parentheses
        i += 1
    return result

# Example Test Cases
test_cases = [
    "(()()) ((())) () ((())())",
    "((()()) )",
    "(()())() ()",
    "((((()))))",
    "(()()())",
    "() ()",
]

for test_case in test_cases:
    expected = parse_nested_parens(test_case)
    print(f"Expected: {expected}")
    actual = [int(i) for i in test_case.map()()]
   +[int(i) for i in expected]
    print(f"Actual: {actual}")
```
This code defines a function `parse_nested_parens` that parses and returns the deepest level of nesting of parentheses in a given string. The function uses a stack data structure to keep track of opening parentheses. It starts by keeping track of the first open parenthesis, then checks to see if there are closing parentheses to match. The function then checks different cases to handle different scenarios: adding to the stack when an opening parenthesis is seen, checking if there are closing parentheses without any nested groups, and adding to the result when there are closing parentheses with nested groups. The stack is used to handle the nesting of the groups. The function returns the expected list of integers representing the deepest level of nesting. 

The test cases demonstrate the usage of the function with different input strings, and the expected and actual results are printed to compare them.