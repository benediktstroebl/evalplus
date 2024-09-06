```python
def separate_paren_groups(s: str) -> List[str]:
    return [p.p for p in s.p if ')' in p and not ')' in p[1:]:
    return []  # Single character and spaces not grouped.

tests = [
    ("() () ()()", ["()", "( )"]),
    ("() ()((()))", ["()", "("])]),
    ("( )  (( ))", ["()", "( )"]),
    ("( )()()  )", ["()"]),
    ("( )()  ()() ", ["()"]),
    ("(() )() ()", ["()", "(()())"]),
    ("( ) ( )()() ", ["()", "( )"]),
    ("( )  (() () )", ["()", "(")]),
    # Different nesting levels
    ("( ) ( )  ( ) ", ["()", "(")]),
]

for test, expected in tests:
    actual = separate_paren_groups(test)
    assert actual == expected
```