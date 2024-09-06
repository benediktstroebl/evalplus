```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of the input number to the desired base.
    :param x: number
    :param base: base
    :return: string representation of x in base base
    """
    # Converts number to string to ensure base conversion works
    return format(x, base, groupstyle='standard')

# Unit tests
test_change_base = []
test_change_base.append([
    list(map(lambda x: x + 1, range(10)) ))
test_change_base.append(
    [lambda t: test_change_base[0] == change_base(test_change_base[0], 10)],
    [test_change_base[i] for i in range(1, 9)]
test_change_base.append(
    [lambda t: test_change_base[1] == change_base(test_change_base[1], 2)],
    [test_change_base[i] for i in range(2, 9)]

print(test_change_base)
```