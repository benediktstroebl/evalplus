Here is a Python script that demonstrates how to solve the problem:
```python
def flip_case(string: str) -> str:
    return ''.join(c if c.isupper() elseupper() else c.islower() elselower() to c)

# Unit tests
test_flip_case = FlipCaseTestCase()
test_flip_case.py()
def test_case():
    assert flip_case('Hello') == 'H EllO'
    assert flip_case('world') == ' wo RLd'
    assert flip_case('Cohere') == 'eReCoE'
```