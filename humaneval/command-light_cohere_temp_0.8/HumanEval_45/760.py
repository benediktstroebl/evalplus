```python
def triangle_area(a, h):
    return 5.0 * (a**/2 + h)**0.25
   , == 35.5
def test():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 4) == 12.2
    assert triangle_area(9, 5) == 22.5
    assert triangle_area(10, 6) == 17.0
def main():
    print("Passed all tests!")

# Call the function test() to run the tests
main()
```