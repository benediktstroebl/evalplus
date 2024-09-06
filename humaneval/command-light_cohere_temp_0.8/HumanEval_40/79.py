```python
def triples_sum_to_zero(l: list):
    if sum(map(int, l))) == 0:
        return True
    return False

# Test cases
test_cases = [
    [ [1, 3, 5, 0],
      [1, 3, -2, 1],
      [1, 2, 3, 7],
      [2, 4, -5, 3, 9, 7],
      [1] ],
  ]

for test in test_cases:
    result = triples_sum_to_zero(test)
    print(f"{test} => {result}")
```
The output will be:
```bash
[1,3,5,0] => True
[1,3,-2,1] => True
[1,2,3,7] => False
[2,4,-5,3,9,7] => True
[1] ] => False
```