```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    # Explicitly using a list comprehension to build the output
    return [i for i, _ in enumerate(s.make_nested_parens(s))]
def make_nested_parens(s: str) -> List[str]:
    # Construct a list of nested parentheses
    return ["(" + s + ")" for s in s.make_parentheses(s)]
def make_parentheses(s: str) -> List[str]:
    # Construct a list of non-nested parentheses
    return ["(" + ")"*len(s)] + [")" for _ in s]
# Unit tests
def test_parse_nested_parens():
    assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
    assert parse_nested_parens("(<<<) ((())) ") == [3]
    assert parse_nested_parens(")>>>" == []
    assert parse_nested_parens(") ((()))") == []
    assert parse_nested_parens("(++)") == []
def main():
    print("Testing parse_nested_parens..." + "\n" + make_nested_parens("()")))
    print("Testing parse_nested_parens..." + "\n" + make_nested_parens("((())")))
    print("Testing parse_nested_parens..." + "\n" + make_nested_parens("(()")))
    print("Testing parse_nested_parens..." + "\n" + make_nested_parens(")()() "))
    print("Testing parse_nested_parens..." + "\n" + make_nested_parens("((((())))))))"
    print("Testing parse_nested_parens..." + "\n" + make_nested_parens("((((((())))))))))))))))"
    print("Testing parse_nested_parens..." + "\n" + make_parentheses("("))
    print("Testing parse_nested_parens..." + "\n" + make_parentheses("()")))
    print("Testing parse_nested_parens..." + "\n" + make_parentheses("""))
    print("Testing parse_nested_parens..." + "\n" + make_parentheses(") "))
    print("Testing parse_nested_parens..." + "\n" + make_parentheses("""))
    print("Testing parse_nested_parens..." + "\n" + make_parentheses("))"))
def main():
    main()
```
The Python script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of their depths of nesting. It also defines two helper functions: `make_nested_parens` which constructs a list of nested parentheses from a string, and `make_parentheses` which constructs a list of non-nested parentheses from a string.

The script then provides unit tests for the `parse_nested_parens` function using `assert` statements, which pass if the function's output matches the expected output. The `main` function is responsible for running the unit tests.