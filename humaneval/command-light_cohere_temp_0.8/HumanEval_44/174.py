```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Base number must be between 2 and 36.")
    result = []
    while x > 0:
        if x % base == 0:
            result.append(str(x[x // base]))
        x //= base
    return ''.join(result)

# Example test cases
test_change_base_pass = [
    [
		[int(j) for j in change_base('8', 3)],
	 [int(j) for j in change_base(8, 2)],
	 [int(j) for j in change_base(7, 2)],
    [int(j) for j in change_base(35, 10)],
    [int(j) for j in change_base(77, 10)],
    [int(j) for j in change_base(8, 12)],
    [int(j) for j in change_base(7, 16)],
    [int(j) for j in change_base(45, 10)],
]

test_change_base_fail = [
    [10, 1],
    [2, 1],
    [7, 2],
    [35, 2],
    [77, 1],
    [88, 3],
]

for case in test_change_base_pass:
    assert case == change_base(*case)
for case in test_change_base_fail:
    try:
        assert change_base(*case) == case[0]
    except AssertionError:
        print("AssertionError:", case)
```